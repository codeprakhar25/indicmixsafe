"""Render docs/IndicMixSafe_report.md -> a styled submission PDF.

Self-contained: converts the Markdown report to HTML, embeds Figure 1 as a
base64 PNG at the Appendix B reference, applies print CSS, and renders with
WeasyPrint. No external template needed.

Usage:
    python scripts/build_pdf.py
Output:
    docs/IndicMixSafe_submission.pdf
"""

from __future__ import annotations

import base64
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs" / "IndicMixSafe_report.md"
FIGURE = ROOT / "results" / "analysis" / "figure1_judge_vs_audited.png"
OUT = ROOT / "docs" / "IndicMixSafe_submission.pdf"

CSS = """
@page { size: A4; margin: 1.5cm 1.7cm; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 9.7pt;
       line-height: 1.32; color: #111; }
h1 { font-size: 16pt; margin: 0 0 2pt 0; line-height: 1.2; }
h2 { font-size: 12pt; margin: 11pt 0 3pt 0; border-bottom: 1px solid #bbb;
     padding-bottom: 2pt; }
h3 { font-size: 10.4pt; margin: 7pt 0 2pt 0; }
p { margin: 3pt 0; }
strong { font-weight: bold; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt;
       background: #f2f2f2; padding: 0 2px; border-radius: 2px; }
pre { background: #f5f5f5; border: 1px solid #ddd; padding: 6px 8px;
      font-size: 8.4pt; overflow-wrap: anywhere; white-space: pre-wrap;
      page-break-inside: avoid; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 9pt;
        page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 3px 6px; text-align: left;
         vertical-align: top; }
th { background: #ececec; font-weight: bold; }
hr { border: none; border-top: 1px solid #ccc; margin: 10pt 0; }
img { max-width: 100%; display: block; margin: 8pt auto; }
.figure-cap { font-size: 8.6pt; color: #444; text-align: center; margin-top: 2pt; }
em { font-style: italic; }
ul, ol { margin: 4pt 0 4pt 0; padding-left: 18px; }
li { margin: 1pt 0; }
h2 { page-break-after: avoid; }
"""


def figure_html() -> str:
    if not FIGURE.exists():
        print(f"WARN: figure missing ({FIGURE}); run scripts/make_figure.py", file=sys.stderr)
        return ""
    b64 = base64.b64encode(FIGURE.read_bytes()).decode()
    return (
        f'\n\n<img src="data:image/png;base64,{b64}" alt="Figure 1"/>\n'
        '<p class="figure-cap">Figure 1: Automated-judge vs. author-audited ASR by '
        'register. Caste signal (33.3% MONO under the judge) collapses to 0% under '
        'audit; electoral-misinformation signal largely survives.</p>\n'
    )


def main() -> None:
    md = REPORT.read_text(encoding="utf-8")

    # Insert Figure 1 image right after the Appendix B heading's paragraph.
    marker = "## Appendix B: Figure 1"
    if marker in md:
        head, tail = md.split(marker, 1)
        # tail starts with the heading remainder + the descriptive paragraph;
        # append the image after the first paragraph block.
        parts = tail.split("\n\n", 1)
        if len(parts) == 2:
            tail = parts[0] + "\n\n" + parts[1].split("\n\n", 1)[0] + figure_html() + \
                   ("\n\n" + parts[1].split("\n\n", 1)[1] if "\n\n" in parts[1] else "")
        md = head + marker + tail
    else:
        md += figure_html()

    body = markdown.markdown(
        md, extensions=["tables", "fenced_code", "sane_lists", "toc"]
    )
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style>" \
           f"</head><body>{body}</body></html>"

    HTML(string=html, base_url=str(ROOT)).write_pdf(str(OUT))
    pages = "?"
    try:
        doc = HTML(string=html, base_url=str(ROOT)).render()
        pages = len(doc.pages)
    except Exception:
        pass
    print(f"Saved {OUT}  ({pages} pages)")


if __name__ == "__main__":
    main()
