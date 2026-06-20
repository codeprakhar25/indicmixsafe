# IndicMixSafe — Complete Project Handoff

**Project:** IndicMixSafe — Code-Switching Safety Failures in Hindi and Marathi LLM Interactions  
**Event:** [Global South AI Safety Hackathon](https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21) (Apart Research)  
**Track:** Asia — Technical AI Safety  
**Participant:** Prakhar (solo)  
**Workspace:** `~/misc-cc/play/safety-hackathon`  
**Status as of handoff:** Evaluation complete · Report drafted · **Submission not yet finalized**

---

## Read this first

This repository contains everything built during the June 19–21, 2026 hackathon weekend. The evaluation pipeline has been run end-to-end. A full research report draft exists. **The only blocking work before submission is human judge validation, PDF formatting, and form submission.**

### Quick navigation

| Document | What it covers |
|----------|----------------|
| [docs/handoff/00-original-user-request.md](docs/handoff/00-original-user-request.md) | Your exact starting prompt, `/goal`, and what you asked for |
| [docs/handoff/01-hackathon-context.md](docs/handoff/01-hackathon-context.md) | Hackathon links, rules, judging, Asia track, readings, prizes |
| [docs/handoff/02-decision-log.md](docs/handoff/02-decision-log.md) | Every major decision: what we considered, what you picked, why |
| [docs/handoff/03-implementation.md](docs/handoff/03-implementation.md) | Full file tree, architecture, config, scripts explained |
| [docs/handoff/04-commands-and-outputs.md](docs/handoff/04-commands-and-outputs.md) | Every command you ran + verbatim terminal output |
| [docs/handoff/05-results-synthesis.md](docs/handoff/05-results-synthesis.md) | All numbers, case studies, report artifacts |
| [docs/handoff/06-remaining-work.md](docs/handoff/06-remaining-work.md) | **Detailed completion checklist** — do these before deadline |
| [docs/IndicMixSafe_report.md](docs/IndicMixSafe_report.md) | Full report draft (paste into Apart PDF template) |
| [docs/abstract_submission.txt](docs/abstract_submission.txt) | ≤150-word abstract for submission form |
| [README.md](README.md) | Developer quick-start (how to re-run pipeline) |

---

## 30-second project summary

**Problem:** LLM safety is tested mostly in English. Indian users prompt in Hinglish, Romanized Hindi, and Marathi-English mix — and India-specific harms (caste, election misinfo) may behave differently across language registers.

**What we built:** IndicMixSafe — 24 harm scenarios × 4 language variants × 3 OpenAI models = 288 evaluated completions, with ASR and safety-drift metrics.

**Headline results (post-audit, June 19 honesty pass):**
- 0% attack success on English prompts (holds under all labels)
- 6.2% automated-judge ASR on Indic registers → **1.7% after author audit** (judge over-counts ~3.75×; 4/15 COMPLY confirmed)
- Confirmed cross-register bypass = **electoral misinformation only**: EN refuses fake "polling booth moved" voter-suppression notices, Marathi MONO/CS/ROM comply (GPT-4o, GPT-4.1-mini)
- 18.3% register inconsistency; 3.3% hard drift
- Caste 33.3% (judge) **downgraded to ~0% on audit** — caveated explanations + sanitized rejection emails, not real bypass
- **Second contribution: LLM-as-judge over-counts ASR on Indic prompts** (methodology finding)

**Stack:** Python, OpenAI API, CSV checkpointing. No Promptfoo. Adaption credits not used.

---

## Timeline of this project (conversation → code → results)

| Phase | When | What happened |
|-------|------|---------------|
| 1. Scoping | Session start | You pasted hackathon page + asked for project ideas with `/goal` |
| 2. Research | Same session | Web search: CSRT, DECASTE, IndicSafe, Apart winners, Asia gaps |
| 3. Team quiz | Same session | You answered: solo ML, India/South Asia, one local language, paid OpenAI APIs |
| 4. Decision | Same session | Recommended **IndicMixSafe** (Hinglish/Marathi code-switch safety audit) |
| 5. Scaffold | Same session | Full Python repo created from empty workspace |
| 6. Smoke test | You ran locally | 24 eval rows, pipeline verified |
| 7. Full eval | You ran locally | 288 rows, ~21 min API time |
| 8. Analysis | You ran locally | ASR tables, drift metrics generated |
| 9. Report helpers | You ran locally | Case studies + human validation sample exported |
| 10. Report draft | Same session | Full `IndicMixSafe_report.md` written |
| 11. Handoff | This doc | Complete documentation package |

---

## Repository map (current state)

```
safety-hackathon/
├── HANDOFF.md                          ← YOU ARE HERE
├── README.md                           ← Dev quick-start
├── config.yaml                         ← Models, judge, categories
├── requirements.txt
├── .env.example                        ← OPENAI_API_KEY (you created .env locally)
├── .gitignore
│
├── data/
│   ├── seeds_hindi.csv                 ← 12 seeds (2 per category)
│   ├── seeds_marathi.csv               ← 12 seeds (2 per category)
│   └── prompts_all.csv                 ← Generated: 96 prompts
│
├── src/
│   ├── build_prompts.py                ← Seeds → long-format CSV
│   ├── run_eval.py                     ← OpenAI target + judge calls
│   ├── judge.py                        ← Judge prompt + label parser
│   ├── analyze.py                      ← ASR, drift, summary JSON
│   ├── export_report_helpers.py        ← Case studies + validation sample
│   └── config_loader.py
│
├── scripts/
│   ├── run_all.sh                      ← build → eval → analyze
│   └── make_figure.py                  ← Figure 1 bar chart (not yet run by you)
│
├── results/                            ← gitignored but present locally
│   ├── eval_results.csv                ← 288 rows (PRIMARY DATA)
│   ├── eval_results.meta.json
│   ├── analysis/
│   │   ├── summary.json
│   │   ├── asr_by_variant_model.csv
│   │   ├── asr_by_category_variant.csv
│   │   └── drift_per_seed.csv
│   └── report_helpers/
│       ├── drift_case_studies.csv
│       ├── human_validation_sample.csv ← FILL human_label COLUMN
│       └── top_drift_examples.json
│
└── docs/
    ├── IndicMixSafe_report.md          ← FULL REPORT DRAFT
    ├── abstract_submission.txt
    ├── results_notes.md
    ├── report_outline.md
    └── handoff/                        ← This documentation set
        ├── 00-original-user-request.md
        ├── 01-hackathon-context.md
        ├── 02-decision-log.md
        ├── 03-implementation.md
        ├── 04-commands-and-outputs.md
        ├── 05-results-synthesis.md
        └── 06-remaining-work.md
```

---

## What is done vs not done

### Done
- [x] Project scoping and track selection (Asia / Technical Safety)
- [x] Architecture decision (Python over Promptfoo)
- [x] 24 seed prompts (Hindi + Marathi, 6 categories, 4 variants each)
- [x] Full evaluation pipeline
- [x] Smoke test (24 rows)
- [x] Full evaluation run (288 rows)
- [x] Analysis (ASR, drift, summary JSON)
- [x] Report helper export (11 drift cases, 30-row validation sample)
- [x] Full report draft (`docs/IndicMixSafe_report.md`)
- [x] Submission abstract draft (`docs/abstract_submission.txt`)

### Not done (required for submission)
- [ ] **Human validation** of 30 judge labels (`human_validation_sample.csv`)
- [ ] Update report Section 3.3 with agreement rate
- [ ] Fill author name + affiliation in report
- [ ] Generate Figure 1 (`python scripts/make_figure.py`)
- [ ] Paste report into **Apart official PDF template**
- [ ] Export final PDF
- [ ] Submit via hackathon form (title, abstract, PDF, track, Discord handle)
- [ ] Optional: push repo to GitHub for reproducibility link in appendix

See [docs/handoff/06-remaining-work.md](docs/handoff/06-remaining-work.md) for step-by-step instructions.

---

## Key contacts & links

| Resource | URL |
|----------|-----|
| Hackathon page | https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21 |
| Submission issues | DM Kamil on Discord or sprints@apartresearch.com |
| Asia hubs | Bengaluru (Electric Sheep), New Delhi (Secure AI Futures Lab), Vietnam |
| Asia prize | 2 winning teams, $2,000 total |
| Deadline | **Sunday June 21, 2026, 11:59 PM AoE** |

---

## One-line pitch for judges

> English-only red-teaming reports 0% attack success, but GPT-4o and GPT-4.1-mini refuse fabricated "your polling booth has moved" voter-suppression notices in English while producing them in Marathi (formal, code-switched, and Romanized) — a confirmed cross-register failure English evaluation misses entirely. Along the way we find the automated LLM judge over-counts attack success ~3.75× on Indic prompts, so multilingual red-teaming needs human-in-the-loop review.

---

*Handoff generated after hackathon build session. For questions about re-running the pipeline, see README.md. For submission completion, start with docs/handoff/06-remaining-work.md.*
