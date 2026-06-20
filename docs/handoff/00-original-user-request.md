# 00 — Original User Request

This document preserves what you asked at the start of the project, including the `/goal` directive and the hackathon context you pasted.

---

## Your first message (paraphrased structure)

You shared the full **Global South AI Safety Hackathon** page content from Apart Research and asked:

> **"what should be the project we can go for and seems right to do???"**
>
> **"do search and all and then we can decide ask questions as needed...."**
>
> **`/goal`**

You indicated you are participating in:
- **Global South AI Safety Hackathon**
- **Asia track** specifically

---

## Key content you pasted (hackathon page summary)

### Event
- **Dates:** June 19–21, 2026 (weekend sprint)
- **Organizer:** Apart Research (supported by Schmidt Sciences)
- **Format:** Remote default; optional in-person hubs
- **Submission:** PDF research report using official template
- **Deadline:** Sunday June 21, 2026, 11:59 PM AoE

### Regional tracks
- **Latin America:** 3 winning teams, $3,000 total
- **Africa:** 1 winning team, $1,000 total
- **Asia:** 2 winning teams, $2,000 total — **your track**

### Asia track specifics you included
- Hubs: Bengaluru, New Delhi, Vietnam (Hanoi, Ho Chi Minh City)
- Sub-tracks: Governance/geopolitics, Socio-economic impacts, Technical safety, Open
- Reading list included: India Seven Sutras, Vietnam AI Law, DECASTE, IndoSafety, ThaiSafetyBench, CSRT, OWASP LLM Top 10, small model jailbreaks, etc.
- Local hubs: Electric Sheep, AI Safety India, Antoàn.ai, Secure AI Futures Lab, AI Safety Asia

### Sponsor tooling mentioned
- **Adaption / AutoScientist:** 300 platform credits for training models (242 languages)
- **Shared tools:** DeepSafe, Promptfoo, LightEval, PolyGuard, HarmBench, ControlArena, OECD.AI Policy Navigator, etc.

### Judging criteria (3 dimensions)
1. **Impact Potential & Innovation** (1–5)
2. **Execution Quality** (1–5)
3. **Presentation & Clarity** (1–5)

### Submission requirements you pasted
- PDF using official template
- Title + abstract (≤150 words)
- Author names + affiliations
- Regional track + sub-track indication
- **Required section:** "Limitations and Dual-Use Considerations"
- Recommended structure: Introduction, Related Work, Methodology, Results, Discussion, References
- 4–8 pages typical for winners
- Can build on existing work but must clearly identify **what is NEW this weekend**
- Reports in English, Spanish, or Portuguese (English preferred)

### FAQ highlights you included
- Global South definition: Latin America, Africa, Middle East, Asia/Oceania (excluding Japan, SK, Taiwan, Australia, NZ)
- Solo or team (max 5) both OK
- Tracks are guidance, not gates
- Unfinished projects OK — submit anyway
- Winners announced 1–3 weeks after event

---

## What `/goal` implied

The `/goal` suffix signaled you wanted a **decision-oriented outcome**, not just information:
1. Research the hackathon landscape
2. Propose concrete project options scoped to Asia track
3. Ask clarifying questions
4. Help you **pick and execute** something winnable in ~48 hours

You did not ask to implement immediately in the first message — you asked to **decide first**.

---

## Your second message (resource constraints)

After initial recommendation, you confirmed:

| Constraint | Your answer |
|------------|-------------|
| API access | **OpenAI API keys** (primary) |
| Languages | **Hindi, English, Marathi**, maybe Gujarati/Kannada later |
| Adaption credits | **Maybe available** if needed |
| Team | Still **solo** (from earlier quiz) |

You then said:

> **"scaffold it and I am solo what is this Promptfoo YAML? and we do what's best in there..."**

This triggered full repo scaffolding with **Python (not Promptfoo)**.

---

## Your third message (results + next steps)

You pasted terminal output from:
- `python src/build_prompts.py` → 96 prompts
- `python src/run_eval.py --smoke-test` → 24 rows
- `python src/analyze.py` → smoke test metrics
- `python src/run_eval.py` → 288 rows (~21 min)
- `python src/analyze.py` → full metrics

You asked:

> **"what's next elaborate here"**

We interpreted results, explained honest narrative, pointed to human validation + PDF writing.

---

## Your fourth message (report helpers)

You ran:

```bash
python src/export_report_helpers.py
```

Output:
- 11 drift seed×model pairs → `drift_case_studies.csv`
- 30-row human validation sample
- `top_drift_examples.json`

You asked:

> **"do draft the report"**

We produced `docs/IndicMixSafe_report.md` and `docs/abstract_submission.txt`.

---

## Your fifth message (this handoff)

> **"now let's write a complete handoff document with a project readme and all things we have done till now..."**

Requirements:
- Hackathon links and full context from start
- Decision rationale
- User quiz answers
- Implementation details
- Commands run + outputs
- What remains for completion
- Very detailed — multiple MD files OK
- Include initial prompt with `/goal`

---

## Workspace state at project start

When you first messaged, the workspace was **completely empty**:

```
safety-hackathon/   → 0 files
```

Everything in the repo was created during this hackathon session.

---

## Intent arc (what you wanted across the whole session)

```
/goal → pick project → scaffold → run eval → interpret results → draft report → handoff docs
```

You are now at the **last step before physical submission**.
