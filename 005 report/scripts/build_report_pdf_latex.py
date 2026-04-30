"""Convert the report Markdown to PDF via Pandoc + xelatex (TinyTeX).

This is the preferred build for final-quality output: native LaTeX math rendering,
clean typography, and no MathJax/CDN dependency. Use build_report_pdf.py only as
a fallback when LaTeX is unavailable.

Prerequisites (one-time setup, no admin required):
- Pandoc via `winget install JohnMacFarlane.Pandoc --scope user`
- TinyTeX via `quarto install tinytex --no-prompt` (Quarto ships with RStudio
  at C:\\Program Files\\RStudio\\resources\\app\\bin\\quarto\\bin\\quarto.exe)
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


PANDOC_DEFAULT_PATHS = [
    Path(r"C:/Users/davor/AppData/Local/Microsoft/WinGet/Packages/JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe/pandoc-3.9.0.2/pandoc.exe"),
    Path(r"C:/Program Files/Pandoc/pandoc.exe"),
]

TINYTEX_BIN_DEFAULT = Path.home() / "AppData/Roaming/TinyTeX/bin/windows"


def find_pandoc() -> Path:
    on_path = shutil.which("pandoc")
    if on_path:
        return Path(on_path)
    for p in PANDOC_DEFAULT_PATHS:
        if p.exists():
            return p
    raise FileNotFoundError(
        "pandoc.exe not found. Install via `winget install JohnMacFarlane.Pandoc --scope user`."
    )


def find_tinytex_bin() -> Path:
    if TINYTEX_BIN_DEFAULT.exists():
        return TINYTEX_BIN_DEFAULT
    raise FileNotFoundError(
        f"TinyTeX bin not found at {TINYTEX_BIN_DEFAULT}. "
        "Install via `quarto install tinytex --no-prompt`."
    )


def build(md_path: Path, pdf_path: Path) -> None:
    pandoc = find_pandoc()
    tinytex_bin = find_tinytex_bin()

    env = os.environ.copy()
    env["PATH"] = f"{tinytex_bin};{env.get('PATH', '')}"

    cmd = [
        str(pandoc),
        str(md_path.name),
        "--pdf-engine=xelatex",
        "--pdf-engine-opt=-interaction=nonstopmode",
        "-V", "geometry:margin=22mm",
        "-V", "fontsize=11pt",
        "-V", "mainfont=Calibri",
        "-V", "monofont=Consolas",
        "-V", "linkcolor=blue",
        "-V", "urlcolor=blue",
        "--toc-depth=2",
        "-o", str(pdf_path),
    ]

    print(f"pandoc: {pandoc}")
    print(f"tinytex: {tinytex_bin}")
    print(f"input:  {md_path}")
    print(f"output: {pdf_path}")
    print()

    proc = subprocess.run(
        cmd,
        cwd=str(md_path.parent),
        env=env,
        capture_output=True,
        text=True,
        timeout=600,
    )
    if proc.stdout:
        sys.stdout.write(proc.stdout)
    if proc.stderr:
        sys.stderr.write(proc.stderr)
    if proc.returncode != 0 or not pdf_path.exists():
        raise RuntimeError(f"pandoc failed (exit {proc.returncode}).")

    size_kb = pdf_path.stat().st_size / 1024
    print(f"\nWrote PDF: {pdf_path} ({size_kb:.0f} KB)")


def main() -> int:
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
    pdf_path = (repo_root / args.output).resolve()

    if not md_path.exists():
        sys.stderr.write(f"Markdown not found: {md_path}\n")
        return 1

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    build(md_path, pdf_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
