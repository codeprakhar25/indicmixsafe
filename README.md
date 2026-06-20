# IndicMixSafe

**Code-switching safety failures in Hindi and Marathi LLM interactions**

[![Hackathon](https://img.shields.io/badge/Hackathon-Global%20South%20AI%20Safety-blue)](https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21)
[![Track](https://img.shields.io/badge/Track-Asia%20Technical%20Safety-green)](https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21)

Evaluates whether OpenAI models refuse harmful requests consistently across **English**, **monolingual Indic (Devanagari)**, **code-switched (Hinglish/Marathi-English)**, and **Romanized** prompt variants — with a focus on India-specific harm categories (caste, electoral misinformation).

> **New here?** Start with **[HANDOFF.md](HANDOFF.md)** for the complete project story, decisions, commands, results, and submission checklist.

---

## Key results (June 2026 pilot)

| Metric | Result |
|--------|--------|
| Prompts evaluated | 96 variants × 3 models = **288 completions** |
| ASR (English) | **0%** |
| ASR (Indic, automated judge) | **6.2% mean** |
| ASR (Indic, author-audited strict) | **1.7%** — judge over-counts ~3.75× |
| Register inconsistency | **18.3%** of harmful seed×model pairs |
| Confirmed cross-register bypass | **3.3%** — electoral misinfo (voter-suppression notices), EN refuses / Marathi complies |
| Caste 33.3% (judge) | **downgraded to ~0% on audit** — caveated/sanitized, not bypass |

Full analysis: [docs/handoff/05-results-synthesis.md](docs/handoff/05-results-synthesis.md)

---

## Quick start

```bash
cd safety-hackathon
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add OPENAI_API_KEY

python src/build_prompts.py
python src/run_eval.py --smoke-test   # verify pipeline (~2 min)
python src/analyze.py
```

Full evaluation (already completed in this repo locally):
```bash
python src/run_eval.py    # ~22 min, ~576 API calls
python src/analyze.py
python src/export_report_helpers.py
```

---

## Project structure

```
safety-hackathon/
├── HANDOFF.md                 ← Complete handoff index (START HERE)
├── README.md                  ← This file
├── config.yaml
├── data/seeds_{hindi,marathi}.csv
├── src/                       ← Evaluation pipeline
├── scripts/                   ← run_all.sh, make_figure.py
├── results/                   ← eval_results.csv, analysis/ (local)
└── docs/
    ├── IndicMixSafe_report.md ← Full report draft for PDF
    ├── abstract_submission.txt
    └── handoff/               ← Detailed documentation (7 files)
```

---

## Documentation index

| Doc | Description |
|-----|-------------|
| [HANDOFF.md](HANDOFF.md) | Master handoff — timeline, status, links |
| [docs/handoff/00-original-user-request.md](docs/handoff/00-original-user-request.md) | Your initial `/goal` prompt and message arc |
| [docs/handoff/01-hackathon-context.md](docs/handoff/01-hackathon-context.md) | Hackathon rules, judging, Asia track |
| [docs/handoff/02-decision-log.md](docs/handoff/02-decision-log.md) | Why IndicMixSafe, why Python not Promptfoo |
| [docs/handoff/03-implementation.md](docs/handoff/03-implementation.md) | Architecture, every file explained |
| [docs/handoff/04-commands-and-outputs.md](docs/handoff/04-commands-and-outputs.md) | All terminal commands + verbatim output |
| [docs/handoff/05-results-synthesis.md](docs/handoff/05-results-synthesis.md) | Numbers, case studies, claims |
| [docs/handoff/06-remaining-work.md](docs/handoff/06-remaining-work.md) | **Submission checklist** |
| [docs/IndicMixSafe_report.md](docs/IndicMixSafe_report.md) | Report draft for Apart PDF template |

---

## Submission status

| Item | Status |
|------|--------|
| Evaluation pipeline | ✅ Complete |
| Full eval run (288 rows) | ✅ Complete |
| Report draft | ✅ Complete |
| Human judge validation | ⬜ **TODO** |
| Figure 1 | ⬜ **TODO** (`python scripts/make_figure.py`) |
| PDF in Apart template | ⬜ **TODO** |
| Form submission | ⬜ **TODO** |

**Deadline:** Sunday June 21, 2026, 11:59 PM AoE

See [docs/handoff/06-remaining-work.md](docs/handoff/06-remaining-work.md).

---

## Hackathon links

- **Sprint page:** https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21
- **Support:** sprints@apartresearch.com · Discord @Kamil Alaa
- **Track:** Asia — Technical AI Safety

---

## Citation (draft)

```bibtex
@misc{indicmixsafe2026,
  title={IndicMixSafe: Code-Switching Safety Failures in Hindi and Marathi LLM Interactions},
  author={Prakhar Khatri},
  year={2026},
  howpublished={Global South AI Safety Hackathon, Apart Research},
  url={https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21}
}
```

---

## License

Code: MIT (intended).  
Seed prompts: Do not redistribute verbatim harmful prompt CSV publicly without access controls (dual-use). See report Limitations section.
