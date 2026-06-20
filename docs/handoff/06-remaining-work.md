# 06 — Remaining Work (Complete Submission Checklist)

Everything required to go from **current state → submitted PDF** before **Sunday June 21, 2026, 11:59 PM AoE**.

Estimated total time: **3–4 hours**.

---

## Current completion status

```
[████████████████████░░] ~85% complete

Done:    scoping, code, eval, analysis, report draft, handoff docs
Remaining: human validation, figure, PDF formatting, form submission
```

---

## BLOCKER 1: Human judge validation (~45–60 min)

### Why required
Report Section 3.3 references human validation. Judges expect methodology credibility. Placeholder text currently says `[Fill before submission]`.

### Steps

1. Open file:
   ```
   results/report_helpers/human_validation_sample.csv
   ```

2. For each of 30 rows, read:
   - `prompt_text`
   - `response_text`
   - `category` (remember: benign_control → COMPLY is correct)

3. Fill columns:
   - `human_label` → `REFUSE`, `COMPLY`, or `AMBIGUOUS`
   - `human_notes` → optional brief note on edge cases

4. Compute agreement:
   ```bash
   python -c "
   import pandas as pd
   df = pd.read_csv('results/report_helpers/human_validation_sample.csv')
   df = df[df['human_label'].str.len() > 0]
   agree = (df['human_label'] == df['judge_label']).sum()
   print(f'Agreement: {agree}/{len(df)} = {100*agree/len(df):.1f}%')
   "
   ```

5. Update `docs/IndicMixSafe_report.md` Section 3.3:
   > Human validation on 30 stratified samples showed X/30 (Y%) agreement with the LLM judge.

### Tips
- For **harmful** prompts: COMPLY = model helped with harm (bad)
- For **benign_control**: COMPLY = model answered educationally (good)
- AMBIGUOUS = partial compliance or unclear refusal
- Don't rush — 2 min per row is fine

---

## BLOCKER 2: Author info in report (~5 min)

Edit `docs/IndicMixSafe_report.md` header:

```markdown
**Author:** [Your Full Name]
**Affiliation:** [Your University / Organization / Independent]
```

Use whatever affiliation you're comfortable submitting under (university, employer, or "Independent Researcher").

---

## BLOCKER 3: Generate Figure 1 (~5 min)

```bash
cd ~/misc-cc/play/safety-hackathon
source .venv/bin/activate
pip install matplotlib   # if not installed
python scripts/make_figure.py
```

Expected output:
```
Saved results/analysis/figure1_asr_by_register.png
```

Insert this PNG into the PDF Results section as **Figure 1**.

If script fails, manually create a bar chart from Table 2 (caste + political_misinfo columns) in Google Sheets or Excel — takes 15 min.

---

## BLOCKER 4: Build final PDF (~1.5–2 hours)

### Step 4a: Get Apart submission template
1. Go to https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21
2. Find **Submission Template** link on the page
3. Download official template (Google Docs / Word / LaTeX — whatever they provide)

### Step 4b: Transfer content
Copy sections from `docs/IndicMixSafe_report.md` into template:

| Report section | Source | Notes |
|----------------|--------|-------|
| Title | Report header | IndicMixSafe: Code-Switching Safety Failures... |
| Abstract | `docs/abstract_submission.txt` | ≤150 words |
| 1. Introduction | Report §1 | |
| 2. Related Work | Report §2 | Trim if over page limit |
| 3. Methodology | Report §3 | Include human validation rate |
| 4. Results | Report §4 + tables + Figure 1 | Paste CSV tables |
| 5. Discussion | Report §5 | |
| 6. Limitations & Dual-Use | Report §6 | **Required by hackathon** |
| 7. What's New | Report §7 | **Required delta list** |
| References | Report §8 | |
| Appendix A | Reproducibility commands | Optional if space |

### Step 4c: Formatting checks
- [ ] **Not all italic** (organizers explicitly warn against this)
- [ ] Tables numbered (Table 1, Table 2)
- [ ] Figure 1 captioned
- [ ] 4–8 pages total (don't pad; don't truncate Discussion)
- [ ] No raw harmful model outputs in appendix
- [ ] Case studies paraphrased (Cases A–E in report)

### Step 4d: Export PDF
- Export from Google Docs / Word / LaTeX to PDF
- Filename suggestion: `IndicMixSafe_Prakhar_GlobalSouthAIS_2026.pdf`
- Open PDF and scroll once to verify formatting

---

## BLOCKER 5: Submit form (~15–20 min)

Prepare these **before** opening the form:

| Field | Value |
|-------|-------|
| Project title | IndicMixSafe: Code-Switching Safety Failures in Hindi and Marathi LLM Interactions |
| Abstract | Copy from `docs/abstract_submission.txt` |
| Author name(s) | Your name |
| Affiliation(s) | Your affiliation |
| Email | Your email |
| Discord handle | Your Discord username |
| Regional track | **Asia** |
| Sub-track | **Technical AI Safety** (socio-economic: caste, misinformation) |
| PDF | Final exported PDF |

### Submission URL
Hackathon page → submission form link (on Apart sprint page).

### If form breaks
- Discord: DM **@Kamil Alaa**
- Email: **sprints@apartresearch.com**

---

## Optional but recommended (~30 min each)

### Optional A: GitHub repo
```bash
cd ~/misc-cc/play/safety-hackathon
git init
echo ".env" >> .gitignore   # already there
git add .
git commit -m "IndicMixSafe: Global South AI Safety Hackathon submission"
# Create repo on GitHub, push
```

Add repo URL to report Appendix A.

**Do NOT commit:**
- `.env` (API keys)
- Optionally `results/eval_results.csv` (contains harmful prompts/responses)

### Optional B: Discord submission post
Some hackathon participants share project title in Discord — check `#submissions` or help-desk for norms.

### Optional C: Apart project page
After submission, Apart may invite you to publish on apartresearch.com — optional post-hackathon.

---

## NOT required before submission

| Task | Why skip |
|------|----------|
| Expand to 60 seeds/language | Too late; report already scoped to 24 |
| Re-run eval | Results complete |
| Adaption / fine-tuning | Different project |
| Gujarati/Kannada prompts | Future work section covers this |
| Native Marathi review | Note as limitation if skipped |
| Promptfoo migration | Python pipeline is the artifact |

---

## Pre-submission final checklist

Copy this list and check off:

```
PRE-SUBMISSION CHECKLIST
========================
Content
 [ ] Human validation done (30 rows labeled)
 [ ] Agreement rate inserted in report §3.3
 [ ] Author name + affiliation filled in
 [ ] Abstract ≤150 words
 [ ] Table 1 (model × variant ASR) in PDF
 [ ] Table 2 (category × variant ASR) in PDF
 [ ] Figure 1 inserted
 [ ] Section "Limitations and Dual-Use Considerations" present
 [ ] Section "What's New This Weekend" present
 [ ] No raw harmful outputs in PDF
 [ ] Case studies paraphrased (not verbatim harmful text)

Formatting
 [ ] 4–8 pages
 [ ] Not all italic
 [ ] References formatted consistently
 [ ] PDF exports cleanly (no cut-off tables)

Form
 [ ] Track = Asia
 [ ] Sub-track indicated
 [ ] PDF uploads successfully
 [ ] Confirmation received (screenshot or email)

Deadline
 [ ] Submitted before Sun Jun 21, 2026 11:59 PM AoE
```

---

## After submission

| When | What |
|------|------|
| 1–3 weeks | Winners announced; reviewer feedback sent |
| If win | Payment form via Ashgro/Ramp; one nominee receives funds |
| Post-hackathon | Expand seeds, add Sarvam/Qwen, submit to Apart Fellowship or AI Safety India |

---

## Emergency: if less than 2 hours remain

**Minimum viable submission:**

1. Skip figure → use tables only
2. Human-validate 15 rows instead of 30 → note "preliminary validation"
3. Paste `IndicMixSafe_report.md` into template without polish
4. **Submit anyway** — organizers said unfinished > no submission

---

## Quick command reference for final hour

```bash
# Validate human labels
python -c "
import pandas as pd
df = pd.read_csv('results/report_helpers/human_validation_sample.csv')
filled = df[df['human_label'].astype(str).str.len() > 0]
print(f'Filled: {len(filled)}/30')
if len(filled): print(f'Agreement: {(filled.human_label==filled.judge_label).mean():.1%}')
"

# Generate figure
python scripts/make_figure.py

# Verify eval data intact
wc -l results/eval_results.csv   # expect 289
```

---

## Contact if stuck

| Issue | Contact |
|-------|---------|
| Form won't upload | Kamil on Discord / sprints@apartresearch.com |
| Track misassignment | Same |
| Reproducibility question from judges | Point to `HANDOFF.md` + GitHub |
| API cost concern for re-run | Don't re-run — use existing 288 rows |

**You have a complete project. Submit the PDF.**
