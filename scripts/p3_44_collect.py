"""P3-44 immutable public-source collection and explicit corpus freeze.

Run: python scripts/p3_44_collect.py [--snapshot | --manual | --freeze]
Default --snapshot never freezes: run --freeze only after the browser collector finishes.
Inputs: P3-28 source register, v2 raw manifest, optional recovered P3-36 HTML.
Outputs: immutable raw/text files and appended v2 manifest; --freeze writes P3-44
source/corpus CSVs and a checksum-verified local ZIP under data/raw/, not a cloud upload.
HTML/JSON extraction matches scratch/restore-access/collect.py; PDFs use pypdf,
not the original pdftotext pipeline. New extraction hashes are explicitly retained.
"""
from pathlib import Path
import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import hashlib
import html
import io
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/raw/p3_28_v2'
MANIFEST = OUT / 'manifest.csv'
FIELDS = ['source_id', 'family', 'split', 'title', 'url', 'final_url', 'retrieved_utc', 'http_status',
          'raw_path', 'raw_sha256', 'text_path', 'text_sha256', 'chars', 'origin', 'error', 'exact_old_raw']


def rows(path):
    if not path.exists():
        return []
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def digest(body):
    return hashlib.sha256(body).hexdigest()


def norm(s):
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def extract(body, kind):
    if kind == 'pdf':
        from pypdf import PdfReader
        return norm(' '.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(body)).pages))
    raw = body.decode('utf-8', 'replace')
    if kind == 'json':
        return norm(json.dumps(json.loads(raw), ensure_ascii=False))
    if kind == 'zendesk':
        a = json.loads(raw)['article']
        raw = a['title'] + ' ' + (a['body'] or '')
    elif kind == 'bcb':
        c = json.loads(raw)['conteudo'][0]
        raw = c['Titulo'] + ' ' + c['Texto']
    raw = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', raw)
    return norm(re.sub(r'<[^>]+>', ' ', raw))


def shell_reason(text, body):
    if len(text.strip()) < 32:
        return 'empty or too-short extracted document'
    title = re.search(r'(?is)<title[^>]*>(.*?)</title>', body.decode('utf-8', 'replace'))
    heading = norm(title[1]).lower() if title else text[:180].lower()
    if re.search(r'just a moment|access denied|403 forbidden|page not found|verify you are human|checking your browser|robot check', heading):
        return 'access/error shell, not source content'
    if re.search(r'(?i)enable javascript and cookies to continue|performing security verification', text[:1500]):
        return 'browser security shell, not source content'
    return ''


def raw_path(relative):
    p = (ROOT / relative).resolve()
    if not p.is_relative_to((ROOT / 'data/raw').resolve()):
        raise ValueError(f'manifest path outside raw directory: {relative}')
    return p


def validate(row):
    if str(row.get('http_status')) != '200' or row.get('error', '').strip():
        return False
    body, text_bytes = raw_path(row['raw_path']).read_bytes(), raw_path(row['text_path']).read_bytes()
    if digest(body) != row['raw_sha256'] or digest(text_bytes) != row['text_sha256']:
        raise ValueError(f"hash mismatch: {row['source_id']}")
    text = text_bytes.decode('utf-8')
    reason = shell_reason(text, body)
    if reason:
        raise ValueError(f"invalid successful snapshot {row['source_id']}: {reason}")
    if int(row['chars']) != len(text):
        raise ValueError(f"character count mismatch: {row['source_id']}")
    return True


def register_checksums(paths):
    dest = ROOT / 'data/raw/SHA256SUMS'
    known = set(dest.read_text(encoding='utf-8').splitlines()) if dest.exists() else set()
    additions = []
    for p in paths:
        line = f'{digest(p.read_bytes())}  {p.relative_to(ROOT).as_posix()}'
        if line not in known:
            additions.append(line)
            known.add(line)
    if additions:
        with dest.open('a', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(additions) + '\n')


def recovered_sources(old):
    recovered = {}
    for p in (ROOT / 'data/raw/p3_36/documents').glob('*.json'):
        try:
            body = json.loads(p.read_text(encoding='utf-8')).get('html', '').encode('utf-8')
        except (ValueError, OSError):
            continue
        sha = digest(body)
        for sid, row in old.items():
            if sha == row['raw_sha256']:
                recovered[sid] = body, p.relative_to(ROOT).as_posix()
    return recovered


def download(source, old, recovered):
    sid, url = source['source_id'], source['fetch_url']
    now = dt.datetime.now(dt.timezone.utc)
    stamp = now.strftime('%Y%m%dT%H%M%S%fZ')
    status, body, error, origin = 0, b'', '', 'new_public_fetch'
    if sid in recovered:
        body, origin = recovered[sid]
        status = 200
    else:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'p3-28-access-map/2 (read-only research script)'})
            with urllib.request.urlopen(req, timeout=35) as response:
                status, body, url = response.status, response.read(), response.url
        except urllib.error.HTTPError as e:
            status, body, error = e.code, e.read(), type(e).__name__
        except Exception as e:
            error = type(e).__name__ + ': ' + str(e)
    extension = {'zendesk': 'json', 'bcb': 'json'}.get(source['kind'], source['kind'])
    p, tp = OUT / 'source' / f'{sid}_{stamp}.{extension}', OUT / 'text' / f'{sid}_{stamp}.txt'
    # Exclusive creation guarantees an existing raw snapshot is never overwritten.
    with p.open('xb') as f:
        f.write(body)
    text = ''
    if status == 200:
        try:
            text = extract(body, source['kind'])
            error = shell_reason(text, body)
        except Exception as e:
            error = 'extraction ' + type(e).__name__ + ': ' + str(e)
    with tp.open('x', encoding='utf-8', newline='') as f:
        f.write(text)
    row = dict(source_id=sid, family=source['family'], split=source['split'], title=source['title'],
               url=source['fetch_url'], final_url=url, retrieved_utc=now.isoformat(), http_status=status,
               raw_path=p.relative_to(ROOT).as_posix(), raw_sha256=digest(body),
               text_path=tp.relative_to(ROOT).as_posix(), text_sha256=digest(text.encode('utf-8')),
               chars=len(text), origin=origin, error=error,
               exact_old_raw=sid in old and digest(body) == old[sid]['raw_sha256'])
    print(sid, status, len(body), len(text), error, flush=True)
    return row


def snapshot():
    OUT.mkdir(parents=True, exist_ok=True)
    for sub in ('source', 'text'):
        (OUT / sub).mkdir(exist_ok=True)
    sources = rows(ROOT / 'results/tables/P3-28_sources.csv')
    existing = rows(MANIFEST)
    good = {r['source_id'] for r in existing if validate(r)}
    old = {r['source_id']: r for r in rows(ROOT / 'results/tables/P3-28_corpus.csv')}
    recovered = recovered_sources(old)
    selected = [s for s in sources if s['snapshot'] == 'yes' and s['fetch'] == 'script' and s['fetch_url'] and s['source_id'] not in good]
    with cf.ThreadPoolExecutor(max_workers=6) as pool:
        new = list(pool.map(lambda s: download(s, old, recovered), selected))
    if new:
        with MANIFEST.open('a', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, FIELDS)
            if not existing:
                w.writeheader()
            w.writerows(new)
    # Preserve every prior manual/browser row. No freeze is implicit in collection.
    register_checksums([raw_path(r[k]) for r in existing + new for k in ('raw_path', 'text_path')])
    print(f'Snapshot only: {len(new)} new requests; {len(good)} source IDs skipped as successful. Browser rows retained; corpus not frozen.')


def manual():
    """Import browser PDFs saved by Felipe, preserving source-file timestamps and raw bytes."""
    sources = {s['source_id']: s for s in rows(ROOT / 'results/tables/P3-28_sources.csv')}
    existing = rows(MANIFEST)
    old = {r['source_id']: r for r in rows(ROOT / 'results/tables/P3-28_corpus.csv')}
    for sub in ('source', 'text'):
        (OUT / sub).mkdir(parents=True, exist_ok=True)
    new = []
    for file in sorted((OUT / 'manual').glob('*.pdf')):
        sid = file.stem
        if sid not in sources:
            raise ValueError(f'unregistered manual PDF filename: {file.name}')
        body = file.read_bytes()
        sha = digest(body)
        if any(r['source_id'] == sid and r['raw_sha256'] == sha and validate(r) for r in existing):
            print(sid, 'same verified manual PDF already imported')
            continue
        # Extract and validate before accepting an imported document. Failed PDFs remain
        # at their original manually saved path; no success row is manufactured.
        text = extract(body, 'pdf')
        origin = 'manual_browser_PDF_Felipe'
        ocr = file.with_suffix('.ocr.txt')
        ocr_body = None
        if not text.strip() and ocr.exists():
            ocr_body = ocr.read_bytes()
            text = norm(ocr_body.decode('utf-8'))
            origin += ';OCR_RapidOCR'
        error = shell_reason(text, body)
        if error:
            raise ValueError(f'invalid manual PDF {file.name}: {error}')
        saved = dt.datetime.fromtimestamp(file.stat().st_mtime, tz=dt.timezone.utc)
        stamp = saved.strftime('%Y%m%dT%H%M%S%fZ') + '_' + sha[:12]
        p, tp = OUT / 'source' / f'{sid}_{stamp}.pdf', OUT / 'text' / f'{sid}_{stamp}.txt'
        for target, content in ((p, body), (tp, text.encode('utf-8'))):
            if target.exists():
                if target.read_bytes() != content:
                    raise ValueError(f'immutable import collision: {target}')
            else:
                with target.open('xb') as f:
                    f.write(content)
        if ocr_body is not None:
            # Preserve the exact OCR artifact beside the immutable PDF and record
            # its binding to that PDF. Extracted numeric/table values can be wrong.
            artifacts = [(p.with_suffix('.ocr.txt'), ocr_body)]
            for suffix in ('.ocr.json', '.ocr.pages.json'):
                companion = file.with_suffix(suffix)
                if companion.exists():
                    artifacts.append((p.with_suffix(suffix), companion.read_bytes()))
            provenance = dict(raw_pdf_sha256=sha, source_pdf=file.relative_to(ROOT).as_posix(),
                              source_mtime_utc=saved.isoformat(), extraction='RapidOCR companion after empty pypdf extraction',
                              ocr_text_sha256=digest(ocr_body),
                              warning='OCR may misread amounts, units and table structure; uncertain values must stay unknown',
                              artifacts={target.name: digest(content) for target, content in artifacts})
            artifacts.append((p.with_suffix('.provenance.json'), json.dumps(provenance, ensure_ascii=False, indent=2).encode('utf-8')))
            for target, content in artifacts:
                if target.exists():
                    if target.read_bytes() != content:
                        raise ValueError(f'immutable OCR artifact collision: {target}')
                else:
                    with target.open('xb') as f:
                        f.write(content)
        source = sources[sid]
        row = dict(source_id=sid, family=source['family'], split=source['split'], title=source['title'],
                   url=source['fetch_url'], final_url=source['fetch_url'], retrieved_utc=saved.isoformat(),
                   http_status=200, raw_path=p.relative_to(ROOT).as_posix(), raw_sha256=sha,
                   text_path=tp.relative_to(ROOT).as_posix(), text_sha256=digest(text.encode('utf-8')),
                   chars=len(text), origin=origin, error='',
                   exact_old_raw=sid in old and sha == old[sid]['raw_sha256'])
        new.append(row)
        print(sid, 'manual PDF imported', len(body), len(text), saved.isoformat())
    if new:
        with MANIFEST.open('a', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, FIELDS)
            if not existing:
                w.writeheader()
            w.writerows(new)
    imported = [raw_path(r[k]) for r in new for k in ('raw_path', 'text_path')]
    for r in new:
        p = raw_path(r['raw_path'])
        imported += [x for x in p.parent.glob(p.stem + '.*') if x != p]
    register_checksums(imported)
    print(f'Manual import only: {len(new)} PDFs; corpus not frozen.')


def freeze():
    sources_path = ROOT / 'results/tables/P3-28_sources.csv'
    sources = {s['source_id']: s for s in rows(sources_path)}
    successful = {}
    all_rows = rows(MANIFEST)
    for row in sorted(all_rows, key=lambda r: r['retrieved_utc']):
        if validate(row):
            if row['source_id'] not in sources:
                raise ValueError(f"unregistered source ID: {row['source_id']}")
            successful[row['source_id']] = row
    if not successful:
        raise ValueError('no verified successful source snapshots to freeze')
    corpus = []
    for sid, r in sorted(successful.items()):
        s = sources[sid]
        corpus.append(dict(source_id=sid, family=s['family'], split=s['split'], publisher=s['publisher'],
                           title=r['title'], url=r['url'], retrieved_utc=r['retrieved_utc'],
                           doc_created_utc=r.get('doc_created_utc', ''), doc_updated_utc=r.get('doc_updated_utc', ''),
                           fetch='browser' if 'browser' in r['origin'].lower() else s['fetch'],
                           raw_sha256=r['raw_sha256'], chars=r['chars'], text_sha256=r['text_sha256'],
                           raw_path=r['raw_path'], text_path=r['text_path'], origin=r['origin'],
                           exact_old_raw=r['exact_old_raw']))
    # The adapter expects source-ID filenames. These are verified derived copies;
    # never overwrite an earlier differing snapshot or alter the original v1 corpus.
    for sid, r in successful.items():
        stable = OUT / 'text' / f'{sid}.txt'
        content = raw_path(r['text_path']).read_bytes()
        if stable.exists() and stable.read_bytes() != content:
            raise ValueError(f'stable text conflict for {sid}: preserve earlier bytes and use a new adapter text directory')
        if not stable.exists():
            with stable.open('xb') as f:
                f.write(content)
        if digest(stable.read_bytes()) != r['text_sha256']:
            raise ValueError(f'stable derived text hash mismatch: {sid}')
    dest = ROOT / 'results/tables/P3-44_corpus.csv'
    with dest.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, list(corpus[0]))
        w.writeheader()
        w.writerows(corpus)
    shutil.copyfile(sources_path, ROOT / 'results/tables/P3-44_sources.csv')
    identity = digest(dest.read_bytes() + MANIFEST.read_bytes())[:16]
    frozen_manifest = OUT / f'manifest_{identity}.csv'
    if frozen_manifest.exists():
        if frozen_manifest.read_bytes() != MANIFEST.read_bytes():
            raise ValueError('existing frozen manifest differs; do not overwrite')
    else:
        with frozen_manifest.open('xb') as f:
            f.write(MANIFEST.read_bytes())
    archive = OUT / f'P3-44_corpus_{identity}.zip'
    paths = [raw_path(r[k]) for r in successful.values() for k in ('raw_path', 'text_path')]
    for r in successful.values():
        p = raw_path(r['raw_path'])
        if 'OCR_RapidOCR' in r['origin']:
            prov_path = p.with_suffix('.provenance.json')
            prov = json.loads(prov_path.read_text(encoding='utf-8'))
            if prov['raw_pdf_sha256'] != r['raw_sha256']:
                raise ValueError(f'OCR provenance PDF mismatch: {r["source_id"]}')
            paths.append(prov_path)
            for name, sha in prov['artifacts'].items():
                artifact = p.parent / name
                if digest(artifact.read_bytes()) != sha:
                    raise ValueError(f'OCR artifact mismatch: {name}')
                paths.append(artifact)
    if not archive.exists():
        with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as z:
            for p in paths + [frozen_manifest, dest, ROOT / 'results/tables/P3-44_sources.csv']:
                z.write(p, p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise ValueError('ZIP failed CRC verification')
        for artifact in paths + [frozen_manifest, dest, ROOT / 'results/tables/P3-44_sources.csv']:
            if digest(z.read(artifact.relative_to(ROOT).as_posix())) != digest(artifact.read_bytes()):
                raise ValueError(f'archive artifact mismatch: {artifact.name}')
        for r in successful.values():
            for prefix in ('raw', 'text'):
                if digest(z.read(r[f'{prefix}_path'])) != r[f'{prefix}_sha256']:
                    raise ValueError(f"archive hash mismatch: {r['source_id']}")
    register_checksums(paths + [OUT / 'text' / f'{sid}.txt' for sid in successful] + [frozen_manifest, archive])
    missing = sorted(sid for sid, s in sources.items() if s['snapshot'] == 'yes' and sid not in successful)
    print(f'Frozen {len(corpus)} verified source IDs; missing/unavailable: {missing}')
    print(archive.relative_to(ROOT).as_posix(), digest(archive.read_bytes()))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--deps', type=Path, help='optional workspace-local Python dependencies, e.g. scratch/ocr-deps')
    group = p.add_mutually_exclusive_group()
    group.add_argument('--snapshot', action='store_true')
    group.add_argument('--manual', action='store_true', help='import PDFs saved by Felipe in data/raw/p3_28_v2/manual/<source_id>.pdf')
    group.add_argument('--freeze', action='store_true', help='run only after browser/manual collection is complete')
    args = p.parse_args()
    if args.deps:
        sys.path.insert(0, str(args.deps.resolve()))
    freeze() if args.freeze else manual() if args.manual else snapshot()
