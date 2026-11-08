"""OCR image-only source PDFs without editing their raw bytes.
Run: python scripts/p3_44_pdf_ocr.py A-30 [A-34] --deps scratch/ocr-deps
Requires PyMuPDF and rapidocr_onnxruntime, installed locally from PyPI.
Writes page images and OCR records under ignored data/raw/p3_28_v2/manual/ocr/;
sidecar <ID>.ocr.txt is derived evidence with PDF SHA-256 provenance, not perfect transcription.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('ids',nargs='+')
    p.add_argument('--deps',default='scratch/ocr-deps')
    args=p.parse_args()
    sys.path.insert(0,str(Path(args.deps).resolve()))
    import pymupdf
    from rapidocr_onnxruntime import RapidOCR
    engine=RapidOCR()
    base=Path('data/raw/p3_28_v2/manual')
    for sid in args.ids:
        src=base/(sid+'.pdf')
        sha=hashlib.sha256(src.read_bytes()).hexdigest()
        folder=base/'ocr'/sid;folder.mkdir(parents=True,exist_ok=True)
        doc=pymupdf.open(src)
        records=[];parts=[]
        for i,page in enumerate(doc):
            dest=folder/f'page_{i+1:02}.png'
            if not dest.exists():page.get_pixmap(matrix=pymupdf.Matrix(2,2)).save(dest)
            result,elapsed=engine(str(dest))
            lines=[{'box':x[0],'text':x[1],'ocr_score':float(x[2])} for x in (result or [])]
            text='\n'.join(x['text'] for x in lines)
            parts.append(f'PAGE {i+1}\n{text}')
            records.append({'page':i+1,'image':dest.as_posix(),'lines':lines,'elapsed':str(elapsed)})
            print(sid,'page',i+1,'of',len(doc),'characters',len(text),flush=True)
        sidecar=base/(sid+'.ocr.txt');out='\n\n'.join(parts)
        if sidecar.exists() and sidecar.read_text(encoding='utf-8')!=out:
            raise ValueError('Existing OCR differs; preserve and version rather than overwrite')
        sidecar.write_text(out,encoding='utf-8')
        meta={'source_pdf':src.as_posix(),'sha256':sha,'engine':'RapidOCR ONNXRuntime','render':'PyMuPDF 2x',
              'warning':'OCR is fallible, especially tables, decimal separators and profile/network qualifiers.',
              'pages':records}
        (folder/'provenance.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':main()
