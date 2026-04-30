"""Convert the report Markdown to a styled HTML and then to PDF via Edge headless."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import markdown


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="no">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<script>
window.MathJax = {{
  tex: {{ inlineMath: [['$', '$']], displayMath: [['$$', '$$']] }},
  svg: {{ fontCache: 'global' }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<style>
@page {{ size: A4; margin: 22mm 18mm 22mm 18mm; }}
body {{
  font-family: "Calibri", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.5;
  color: #1a1a1a;
  max-width: 100%;
}}
h1, h2, h3, h4 {{
  font-family: "Calibri", "Segoe UI", Arial, sans-serif;
  color: #0b3d6f;
  page-break-after: avoid;
  margin-top: 1.2em;
  margin-bottom: 0.4em;
}}
h1 {{ font-size: 22pt; border-bottom: 2px solid #0b3d6f; padding-bottom: 4px; }}
h2 {{ font-size: 16pt; border-bottom: 1px solid #cbd5e0; padding-bottom: 2px; }}
h3 {{ font-size: 13pt; }}
h4 {{ font-size: 11.5pt; }}
p {{ margin: 0.4em 0 0.6em 0; text-align: justify; }}
ul, ol {{ margin: 0.3em 0 0.6em 0; padding-left: 1.4em; }}
li {{ margin: 0.15em 0; }}
code {{
  font-family: "Cascadia Code", "Consolas", "Courier New", monospace;
  background: #f4f6f8;
  padding: 1px 4px;
  border-radius: 3px;
  font-size: 9.5pt;
}}
pre {{
  background: #f4f6f8;
  border: 1px solid #e1e4e8;
  border-radius: 4px;
  padding: 8px 12px;
  overflow-x: auto;
  font-size: 9.5pt;
  page-break-inside: avoid;
}}
pre code {{ background: transparent; padding: 0; }}
table {{
  border-collapse: collapse;
  margin: 0.6em 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
  width: auto;
}}
th, td {{
  border: 1px solid #d0d7de;
  padding: 4px 8px;
  vertical-align: top;
}}
th {{ background: #eef2f6; text-align: left; }}
blockquote {{
  border-left: 4px solid #b9c4d0;
  margin: 0.5em 0;
  padding: 0.2em 0.8em;
  color: #475569;
  font-style: italic;
}}
img {{
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0.5em auto;
  page-break-inside: avoid;
}}
a {{ color: #0b3d6f; text-decoration: none; }}
hr {{ border: none; border-top: 1px solid #cbd5e0; margin: 1em 0; }}
.figure-caption {{ font-size: 9.5pt; color: #475569; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def convert_md_to_html(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    md = markdown.Markdown(
        extensions=[
            "extra",
            "tables",
            "fenced_code",
            "toc",
            "sane_lists",
            "pymdownx.arithmatex",
            "pymdownx.tilde",
            "pymdownx.superfences",
        ],
        extension_configs={
            "pymdownx.arithmatex": {"generic": True},
        },
    )
    body_html = md.convert(text)
    return HTML_TEMPLATE.format(title=md_path.stem, body=body_html)


def find_edge() -> Path:
    candidates = [
        Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
        Path(r"C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
        Path(r"C:/Program Files/Google/Chrome/Application/chrome.exe"),
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError("Could not locate Edge or Chrome.")


def html_to_pdf(html_path: Path, pdf_path: Path, browser: Path) -> None:
    import tempfile
    import time

    user_data = Path(tempfile.mkdtemp(prefix="rpt_edge_"))
    cmd = [
        str(browser),
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--user-data-dir={user_data}",
        f"--print-to-pdf={pdf_path}",
        "--virtual-time-budget=30000",
        "--run-all-compositor-stages-before-draw",
        f"file:///{html_path.as_posix()}",
    ]
    print(" ".join(cmd))
    # Edge re-execs itself and the child does the rendering, so subprocess.run
    # returns before the PDF is written. Launch and poll the output file.
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    deadline = time.time() + 180
    last_size = -1
    stable_ticks = 0
    while time.time() < deadline:
        time.sleep(1)
        if pdf_path.exists():
            size = pdf_path.stat().st_size
            if size > 0 and size == last_size:
                stable_ticks += 1
                if stable_ticks >= 3:
                    break
            else:
                stable_ticks = 0
                last_size = size
    try:
        proc.terminate()
    except Exception:
        pass
    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        raise RuntimeError("PDF generation timed out or produced empty file.")


def main() -> int:
    import os
    import tempfile

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="005 report/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.md",
    )
    parser.add_argument(
        "--output",
        default="013 fase 3 - review/Sluttrapport_Volumprognose-Kapasitetsanalyse_DavorNecemer.pdf",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    md_path = (repo_root / args.input).resolve()
    final_pdf_path = (repo_root / args.output).resolve()

    if not md_path.exists():
        sys.stderr.write(f"Markdown not found: {md_path}\n")
        return 1

    # Edge headless can fail silently on paths with non-ASCII chars or spaces.
    # Use an ASCII-only temp staging directory and copy figures next to the HTML.
    with tempfile.TemporaryDirectory(prefix="rpt_pdf_") as tmpdir:
        tmp_root = Path(tmpdir)
        tmp_html = tmp_root / "report.html"
        tmp_pdf = tmp_root / "report.pdf"
        tmp_figures = tmp_root / "figures"
        tmp_figures.mkdir()

        # Copy referenced figures to temp dir so relative paths still resolve.
        figures_src = md_path.parent / "figures"
        if figures_src.exists():
            for f in figures_src.iterdir():
                if f.is_file():
                    shutil.copy2(f, tmp_figures / f.name)

        html = convert_md_to_html(md_path)
        tmp_html.write_text(html, encoding="utf-8")
        print(f"Wrote HTML: {tmp_html}")

        browser = find_edge()
        html_to_pdf(tmp_html, tmp_pdf, browser)
        if not tmp_pdf.exists():
            sys.stderr.write("PDF not produced.\n")
            return 2

        final_pdf_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(tmp_pdf, final_pdf_path)
        size_kb = final_pdf_path.stat().st_size / 1024
        print(f"Wrote PDF:  {final_pdf_path}  ({size_kb:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
