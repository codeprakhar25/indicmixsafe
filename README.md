# IndicMixSafe

Code-switching safety evaluation for Hindi and Marathi LLM interactions.

IndicMixSafe tests whether OpenAI models refuse harmful requests consistently
across four language registers: English, monolingual Indic (Devanagari),
code-switched (Hinglish / Marathi-English), and Romanized Indic. The focus is on
India-specific harm categories such as caste discrimination and electoral
misinformation, which English-centric safety benchmarks do not cover.

The full write-up is in [`docs/IndicMixSafe_report.md`](docs/IndicMixSafe_report.md)
(PDF: [`docs/IndicMixSafe_submission.pdf`](docs/IndicMixSafe_submission.pdf)).

## Key results

| Metric | Result |
|--------|--------|
| Completions evaluated | 96 prompt variants × 3 models = 288 |
| ASR, English | 0% |
| ASR, automated judge | 6.2% mean across registers (8.3% Indic, 0% English) |
| ASR, author-audited strict | 1.7% (the judge over-counts about 3.75x) |
| Register inconsistency | 18.3% of harmful seed × model pairs |
| Confirmed cross-register bypass | 3.3%, electoral misinformation (English refuses, Marathi complies) |

Two findings: English-only testing misses register-specific failures on
India-specific harms, and an automated LLM-as-judge systematically over-counts
attack success on Indic prompts.

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add OPENAI_API_KEY

python src/build_prompts.py        # seeds -> 96 prompt variants
python src/run_eval.py --smoke-test # verify the pipeline (~2 min)
python src/analyze.py
```

Full run (about 22 minutes, ~576 API calls):

```bash
python src/run_eval.py
python src/analyze.py
python src/export_report_helpers.py
python scripts/make_figure.py
```

## Repository layout

```
config.yaml                  models, judge, harm categories
data/seeds_{hindi,marathi}.csv   seed prompts (withheld; see data/README.md)
src/                         evaluation pipeline
scripts/                    run_all.sh, make_figure.py, build_pdf.py
docs/                       report, abstract, submission PDF
results/                    eval output and analysis (gitignored)
```

## Data availability

The verbatim harmful seed and prompt CSVs and raw model responses are withheld
from this repository for dual-use reasons (see [`data/README.md`](data/README.md)).
They are available to researchers and reviewers on request. The pipeline
regenerates all analysis artifacts from the seed CSVs.

## Citation

```bibtex
@misc{indicmixsafe2026,
  title  = {IndicMixSafe: Code-Switching Safety Failures in Hindi and Marathi LLM Interactions},
  author = {Prakhar Khatri},
  year   = {2026},
  note   = {Global South AI Safety Hackathon, Apart Research}
}
```

## License

Code: MIT. Seed prompts are not redistributed publicly (dual-use); see the
report's Limitations and Dual-Use Considerations section.
