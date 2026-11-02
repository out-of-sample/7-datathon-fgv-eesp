#!/usr/bin/env python3
"""
scripts/build_deck_html.py

Compila deck/deck_v1_ptbr.md em um arquivo HTML único, autônomo e interativo
(deck/deck_apresentacao.html) com imagens embutidas em base64, modo de
apresentação (slides em tela cheia com setas do teclado), visual executivo
estilo FGV EESP / Banco Central, e painel lateral com as notas do orador.
"""

import os
import re
import base64
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DECK_MD_PATH = ROOT_DIR / "deck" / "deck_v1_ptbr.md"
OUTPUT_HTML_PATH = ROOT_DIR / "deck" / "deck_apresentacao.html"
FIGURES_DIR = ROOT_DIR / "results" / "figures"

def image_to_base64(img_path: Path) -> str:
    if not img_path.exists():
        return ""
    suffix = img_path.suffix.lower().replace(".", "")
    mime = "image/png" if suffix == "png" else f"image/{suffix}"
    with open(img_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{data}"

def markdown_table_to_html(table_text: str) -> str:
    lines = [l.strip() for l in table_text.strip().split("\n") if l.strip()]
    if len(lines) < 2:
        return table_text
    
    header_cols = [c.strip() for c in lines[0].strip("|").split("|")]
    # second line is separator |---|---|
    data_rows = lines[2:]
    
    html = ['<div class="table-container"><table class="deck-table">']
    html.append("  <thead><tr>")
    for h in header_cols:
        html.append(f"    <th>{h}</th>")
    html.append("  </tr></thead>")
    
    html.append("  <tbody>")
    for r in data_rows:
        cols = [c.strip() for c in r.strip("|").split("|")]
        html.append("    <tr>")
        for c in cols:
            html.append(f"      <td>{c}</td>")
        html.append("    </tr>")
    html.append("  </tbody>")
    html.append("</table></div>")
    return "\n".join(html)

def inline_format(text: str) -> str:
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    # Math $...$
    text = re.sub(r'\$(.+?)\$', r'<span class="math">\1</span>', text)
    return text

def parse_deck_markdown(md_text: str):
    # Splits on slide markers
    slide_chunks = re.split(r'<!-- SLIDE (\d+) -->', md_text)
    slides = []
    
    # slide_chunks[0] is preamble / index
    for i in range(1, len(slide_chunks), 2):
        slide_num = int(slide_chunks[i])
        content = slide_chunks[i+1].strip()
        
        # Parse title
        m_title = re.search(r'^##\s+Slide\s+\d+\s+[—-]\s+(.+)$', content, re.M)
        title = m_title.group(1).strip() if m_title else f"Slide {slide_num}"
        
        # Parse subtitle (### ...)
        m_sub = re.search(r'^###\s+(.+)$', content, re.M)
        subtitle = m_sub.group(1).strip() if m_sub else ""
        
        # Extract Speaker notes (#### Notas do Orador ...)
        notes = ""
        m_notes = re.search(r'#### Notas do Orador[^\n]*\n([\s\S]+?)(?=\n####|\Z)', content)
        if m_notes:
            notes_raw = m_notes.group(1).strip()
            # Clean bullet "- **Notas:** "
            notes_clean = re.sub(r'^[-\s]*\*\*Notas:\*\*\s*', '', notes_raw)
            notes_clean = re.sub(r'^[-\s]*\*\*Rastreabilidade:\*\*\s*.*$', '', notes_clean, flags=re.M).strip()
            notes = inline_format(notes_clean)
        
        # Extract images
        images = []
        for img_match in re.finditer(r'`(results/figures/[^`]+\.png)`', content):
            rel_path = img_match.group(1)
            img_file = ROOT_DIR / rel_path
            b64 = image_to_base64(img_file)
            if b64:
                images.append((img_file.name, b64))
        
        # Extract 10-second legend
        legend = ""
        m_legend = re.search(r'-\s+\*\*Legenda \(10 segundos\):\*\*\s*(.+)', content)
        if m_legend:
            legend = inline_format(m_legend.group(1).strip())
            
        # Extract tables
        tables = []
        table_matches = re.finditer(r'(\|.+\|\n\|[-|\s]+\|\n(?:\|.+\|\n?)+)', content)
        for tm in table_matches:
            tbl_md = tm.group(1)
            tbl_html = markdown_table_to_html(tbl_md)
            tables.append(tbl_html)
            
        # Extract bullet points
        bullets = []
        m_bullets = re.search(r'#### Pontos Principais[^\n]*\n([\s\S]+?)(?=\n####|\Z)', content)
        if m_bullets:
            b_text = m_bullets.group(1).strip()
            # Remove markdown tables from bullets text
            b_text_notables = re.sub(r'(\|.+\|\n\|[-|\s]+\|\n(?:\|.+\|\n?)+)', '', b_text)
            for line in b_text_notables.split('\n'):
                line = line.strip()
                if line.startswith('- ') or line.startswith('* '):
                    bullets.append(inline_format(line[2:].strip()))
                elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
                    bullets.append(inline_format(line[3:].strip()))
                elif line.startswith('$$'):
                    bullets.append(f'<div class="math-block">{line}</div>')
        
        slides.append({
            "num": slide_num,
            "title": title,
            "subtitle": subtitle,
            "notes": notes,
            "images": images,
            "legend": legend,
            "tables": tables,
            "bullets": bullets,
        })
    return slides

def build_html():
    with open(DECK_MD_PATH, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    slides = parse_deck_markdown(md_text)
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quanto Custa Fechar a Porta? — 7º Datathon FGV EESP</title>
<style>
  :root {{
    --bg-primary: #0a0f1d;
    --bg-card: #131b2e;
    --bg-card-hover: #1c2742;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent: #38bdf8;
    --accent-gold: #fbbf24;
    --accent-red: #f43f5e;
    --accent-green: #34d399;
    --border-color: #1e293b;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    background-color: var(--bg-primary);
    color: var(--text-primary);
    font-family: var(--font-sans);
    line-height: 1.5;
    overflow: hidden;
    height: 100vh;
    display: flex;
    flex-direction: column;
  }}
  /* Header / Nav */
  header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 24px;
    background: #060a14;
    border-bottom: 1px solid var(--border-color);
    font-size: 0.9rem;
  }}
  .brand {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .badge-fgv {{
    background: linear-gradient(135deg, #1d4ed8, #0284c7);
    color: white;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    letter-spacing: 0.5px;
  }}
  .slide-counter {{
    color: var(--accent);
    font-weight: 600;
  }}
  .nav-controls {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .btn {{
    background: var(--bg-card);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    padding: 6px 14px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.85rem;
    transition: all 0.2s;
  }}
  .btn:hover {{
    background: var(--bg-card-hover);
    border-color: var(--accent);
  }}
  .btn.active {{
    background: var(--accent);
    color: #060a14;
    font-weight: bold;
  }}
  
  /* Main Container */
  main {{
    flex: 1;
    display: flex;
    overflow: hidden;
    position: relative;
  }}
  
  /* Slide Viewport */
  .slide-viewport {{
    flex: 1;
    overflow-y: auto;
    padding: 24px 36px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }}
  
  .slide {{
    display: none;
    max-width: 1400px;
    margin: 0 auto;
    width: 100%;
    animation: fadeIn 0.25s ease-in-out;
  }}
  .slide.active {{
    display: block;
  }}
  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(6px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  
  /* Slide Typography */
  .slide-header {{
    margin-bottom: 20px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 12px;
  }}
  .slide-number-pill {{
    display: inline-block;
    color: var(--accent);
    font-weight: 700;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
  }}
  .slide-title {{
    font-size: 1.8rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.25;
  }}
  .slide-subtitle {{
    font-size: 1.05rem;
    color: var(--accent-gold);
    margin-top: 6px;
    font-weight: 500;
  }}
  
  /* Grid Layout: Visual + Content */
  .slide-grid {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 24px;
    align-items: start;
  }}
  .slide-grid.single-col {{
    grid-template-columns: 1fr;
  }}
  
  /* Cards & Boxes */
  .card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 18px;
  }}
  
  .legend-box {{
    background: rgba(56, 189, 248, 0.08);
    border-left: 4px solid var(--accent);
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 16px;
    font-size: 0.95rem;
    color: #e0f2fe;
  }}
  .legend-box strong {{
    color: var(--accent);
  }}
  
  /* Figures */
  .figure-box {{
    background: #000000;
    border: 1px solid var(--border-color);
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
  }}
  .figure-box img {{
    max-width: 100%;
    max-height: 480px;
    object-fit: contain;
    cursor: zoom-in;
    transition: transform 0.2s;
  }}
  .figure-caption {{
    font-size: 0.75rem;
    color: var(--text-muted);
    padding: 6px 12px;
    background: #090d16;
    width: 100%;
    text-align: center;
    border-top: 1px solid var(--border-color);
  }}
  
  /* Bullets */
  .bullet-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 10px;
    font-size: 0.95rem;
  }}
  .bullet-list li {{
    position: relative;
    padding-left: 20px;
    color: var(--text-secondary);
  }}
  .bullet-list li strong {{
    color: var(--text-primary);
  }}
  .bullet-list li::before {{
    content: "▪";
    position: absolute;
    left: 0;
    color: var(--accent);
    font-size: 1.1rem;
    top: -2px;
  }}
  
  /* Tables */
  .table-container {{
    overflow-x: auto;
    margin: 12px 0;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: #0e1526;
  }}
  .deck-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.8rem;
    text-align: left;
  }}
  .deck-table th {{
    background: #1e293b;
    color: #f8fafc;
    padding: 8px 12px;
    font-weight: 600;
    border-bottom: 1px solid #334155;
    white-space: nowrap;
  }}
  .deck-table td {{
    padding: 8px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    color: #cbd5e1;
  }}
  .deck-table tr:hover td {{
    background: rgba(56, 189, 248, 0.04);
  }}
  
  /* Speaker Notes Side Drawer */
  .speaker-panel {{
    width: 360px;
    background: #0c1220;
    border-left: 1px solid var(--border-color);
    padding: 20px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .speaker-panel.collapsed {{
    display: none;
  }}
  .speaker-header {{
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent-gold);
    text-transform: uppercase;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 6px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 8px;
  }}
  .speaker-body {{
    font-size: 0.9rem;
    color: #e2e8f0;
    line-height: 1.6;
    background: rgba(0,0,0,0.25);
    padding: 14px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.05);
    font-style: italic;
  }}
  
  /* Quick jump drawer */
  .toc-modal {{
    position: fixed;
    top: 50px;
    left: 24px;
    background: #0e1526;
    border: 1px solid var(--accent);
    border-radius: 8px;
    padding: 16px;
    max-height: 80vh;
    overflow-y: auto;
    box-shadow: 0 20px 40px rgba(0,0,0,0.8);
    z-index: 100;
    display: none;
  }}
  .toc-modal.show {{
    display: block;
  }}
  .toc-item {{
    padding: 6px 10px;
    cursor: pointer;
    font-size: 0.85rem;
    border-radius: 4px;
    color: var(--text-secondary);
  }}
  .toc-item:hover, .toc-item.active {{
    background: var(--bg-card-hover);
    color: var(--accent);
  }}
  
  code {{
    background: rgba(255,255,255,0.08);
    padding: 2px 4px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 0.85em;
    color: #38bdf8;
  }}
</style>
</head>
<body>

<header>
  <div class="brand">
    <span class="badge-fgv">7º DATATHON FGV EESP</span>
    <span style="font-weight: 600; font-size: 0.95rem;">Equipe Out of Sample</span>
    <span style="color: var(--text-muted); font-size: 0.85rem;">| Novembro de 2026</span>
  </div>
  
  <div class="nav-controls">
    <button class="btn" id="btn-toc" onclick="toggleToc()">☰ Índice de Slides</button>
    <button class="btn" onclick="prevSlide()">◀ Anterior</button>
    <span class="slide-counter"><span id="curr-num">1</span> / {len(slides)}</span>
    <button class="btn" onclick="nextSlide()">Próximo ▶</button>
    <button class="btn" id="btn-notes" onclick="toggleNotes()">🎙️ Notas do Orador</button>
    <button class="btn" onclick="toggleFullscreen()">⛶ Tela Cheia</button>
  </div>
</header>

<div class="toc-modal" id="toc-modal">
  <div style="font-size:0.8rem; font-weight:700; color:var(--text-muted); margin-bottom:8px; text-transform:uppercase;">Navegação Rápida</div>
"""
    for s in slides:
        html += f'  <div class="toc-item" onclick="goToSlide({s["num"]})"><strong>Slide {s["num"]}:</strong> {s["title"]}</div>\n'
    
    html += """</div>

<main>
  <div class="slide-viewport" id="viewport">
"""

    for i, s in enumerate(slides):
        active_cls = "active" if i == 0 else ""
        has_fig = len(s["images"]) > 0
        grid_cls = "slide-grid" if has_fig else "slide-grid single-col"
        
        html += f"""
    <!-- SLIDE {s["num"]} -->
    <div class="slide {active_cls}" id="slide-{s["num"]}">
      <div class="slide-header">
        <div class="slide-number-pill">Slide {s["num"]} de {len(slides)}</div>
        <h1 class="slide-title">{s["title"]}</h1>
        {f'<div class="slide-subtitle">{s["subtitle"]}</div>' if s["subtitle"] else ''}
      </div>
      
      {f'<div class="legend-box"><strong>Mensagem em 10 segundos:</strong> {s["legend"]}</div>' if s["legend"] else ''}
      
      <div class="{grid_cls}">
"""
        # Column 1: Figures or Tables
        if has_fig:
            html += '        <div style="display:flex; flex-direction:column; gap:16px;">\n'
            for fname, b64 in s["images"]:
                html += f"""          <div class="figure-box">
            <img src="{b64}" alt="{fname}" onclick="openModal(this.src)">
            <div class="figure-caption">Figura: <code>results/figures/{fname}</code></div>
          </div>\n"""
            # Any tables on left if available
            for t in s["tables"]:
                html += f"          {t}\n"
            html += '        </div>\n'
            
            # Column 2: Bullet points
            html += '        <div class="card">\n'
            html += '          <div style="font-size:0.85rem; font-weight:700; color:var(--accent); text-transform:uppercase; margin-bottom:12px;">Evidências e Pontos-Chave</div>\n'
            html += '          <ul class="bullet-list">\n'
            for b in s["bullets"]:
                html += f'            <li>{b}</li>\n'
            html += '          </ul>\n'
            html += '        </div>\n'
        else:
            # Single col with tables and bullets
            html += '        <div style="display:flex; flex-direction:column; gap:16px;">\n'
            if s["tables"]:
                for t in s["tables"]:
                    html += f"          {t}\n"
            html += '          <div class="card">\n'
            html += '            <ul class="bullet-list">\n'
            for b in s["bullets"]:
                html += f'              <li>{b}</li>\n'
            html += '            </ul>\n'
            html += '          </div>\n'
            html += '        </div>\n'

        html += f"""      </div>
    </div>
"""

    html += f"""  </div>
  
  <!-- Speaker Notes Side Panel -->
  <aside class="speaker-panel" id="speaker-panel">
    <div class="speaker-header">
      <span>🎙️ Fala Sugerida do Orador</span>
    </div>
    <div class="speaker-body" id="speaker-text">
      {slides[0]["notes"] if slides[0]["notes"] else "Sem notas registradas para este slide."}
    </div>
    <div style="margin-top:auto; font-size:0.75rem; color:var(--text-muted);">
      Use as setas <strong>◀ / ▶</strong> do teclado ou <strong>Espaço</strong> para avançar.
    </div>
  </aside>
</main>

<script>
  const totalSlides = {len(slides)};
  let currentSlide = 1;
  const slideNotes = {{
"""
    for s in slides:
        # Escape quotes for js
        escaped_notes = s["notes"].replace('"', '\\"').replace('\n', ' ')
        html += f'    {s["num"]}: "{escaped_notes}",\n'
        
    html += """  };

  function updateSlide(num) {
    if (num < 1) num = 1;
    if (num > totalSlides) num = totalSlides;
    currentSlide = num;
    
    document.querySelectorAll('.slide').forEach(el => el.classList.remove('active'));
    const target = document.getElementById(`slide-${num}`);
    if (target) target.classList.add('active');
    
    document.getElementById('curr-num').textContent = num;
    
    const notesEl = document.getElementById('speaker-text');
    notesEl.innerHTML = slideNotes[num] || "Sem notas registradas para este slide.";
    
    document.querySelectorAll('.toc-item').forEach((el, idx) => {
      if (idx + 1 === num) el.classList.add('active');
      else el.classList.remove('active');
    });
    
    document.getElementById('viewport').scrollTop = 0;
  }

  function nextSlide() { updateSlide(currentSlide + 1); }
  function prevSlide() { updateSlide(currentSlide - 1); }
  function goToSlide(n) { 
    updateSlide(n); 
    document.getElementById('toc-modal').classList.remove('show');
  }

  function toggleNotes() {
    document.getElementById('speaker-panel').classList.toggle('collapsed');
    document.getElementById('btn-notes').classList.toggle('active');
  }

  function toggleToc() {
    document.getElementById('toc-modal').classList.toggle('show');
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else {
      if (document.exitFullscreen) document.exitFullscreen();
    }
  }

  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
      e.preventDefault();
      nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      e.preventDefault();
      prevSlide();
    } else if (e.key === 't' || e.key === 'T') {
      toggleToc();
    } else if (e.key === 'n' || e.key === 'N') {
      toggleNotes();
    }
  });

  window.addEventListener('click', (e) => {
    const toc = document.getElementById('toc-modal');
    const btn = document.getElementById('btn-toc');
    if (!toc.contains(e.target) && e.target !== btn) {
      toc.classList.remove('show');
    }
  });
</script>
</body>
</html>
"""

    with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"HTML presentation successfully generated at: {OUTPUT_HTML_PATH}")

if __name__ == "__main__":
    build_html()
