# 01 — Hackathon Context (Complete Reference)

All information relevant to the Global South AI Safety Hackathon as it pertained to this project.

---

## Primary links

| Item | URL |
|------|-----|
| **Hackathon sprint page** | https://apartresearch.com/sprints/global-south-ais-hackathon-2026-06-19-to-2026-06-21 |
| **Apart Research** | https://apartresearch.com |
| **Support email** | sprints@apartresearch.com |
| **Discord** | Invite linked on hackathon page (help-desk: tag @Kamil Alaa) |

---

## Event overview

| Field | Value |
|-------|-------|
| Name | Global South AI Safety Hackathon |
| Dates | **June 19–21, 2026** (starts Friday evening) |
| Submission deadline | **Sunday June 21, 2026, 11:59 PM AoE** (Anywhere on Earth) |
| Format | Weekend research sprint — build + write PDF report |
| Default mode | Remote (hubs optional) |
| Organizer | Apart Research |
| Sponsor mention | Schmidt Sciences; Adaption (training credits) |

---

## Eligibility (Asia track)

Per hackathon FAQ (Britannica Global South definition):

**In scope:** Latin America, Africa, Middle East, Asia/Oceania **excluding** Japan, South Korea, Taiwan, Australia, New Zealand.

**Out of region:** Can submit to Open Track (Track 4).

**Requirements:** No formal research or coding background required. Ability to scope a small experiment and write a clear PDF is what matters.

**Team:** Solo or up to 5 people. You compete in the regional track you select.

---

## Asia track details

### Prize
- **2 winning teams**
- **$2,000 total** prize pool for Asia

### In-person hubs (optional)
- **Bengaluru** — Electric Sheep
- **New Delhi** — Secure AI Futures Lab
- **Vietnam** — Hanoi and Ho Chi Minh City (Antoàn.ai)

### Sub-tracks (guidance only — not gates)
1. **Governance and geopolitics** — AI compliance, sovereignty, compute access
2. **Socio-economic impacts** — deepfakes, caste bias, rural healthcare AI, gig labor
3. **Technical safety** — multilingual eval, small/edge models, cybersecurity, jailbreaks
4. **Open** — anything relevant to regional AI safety

### Our sub-track selection
**Primary:** Technical safety (multilingual evaluation, code-switching red-teaming)  
**Cross-tag:** Socio-economic impacts (caste, electoral misinformation)

---

## Judging criteria (full rubric summary)

### Dimension 1: Impact Potential & Innovation
- Score 4–5 requires genuinely new contribution, not replicating recent work
- Neglected regional problems score higher
- Clear theory of change helps

### Dimension 2: Execution Quality
- Sound methodology, interpretable results
- For hackathon: **clear delta of what's new this weekend**
- Limitations acknowledged

### Dimension 3: Presentation & Clarity
- Problem, method, findings, limitations must be extractable quickly
- 4–8 page reports typical for winners

---

## Submission requirements (checklist from hackathon page)

### Must include
- [ ] PDF in **official Apart submission template**
- [ ] Project title
- [ ] Abstract (≤150 words)
- [ ] Author names + affiliations
- [ ] Regional track + sub-track
- [ ] Section: **"Limitations and Dual-Use Considerations"**

### Recommended report sections
1. Introduction — problem + why it matters for region
2. Related Work
3. Methodology — replicable detail
4. Results — quantitative where possible
5. Discussion — implications, limitations, future work
6. References

### Important notes from organizers
- Do **not** submit entire report in italic
- Can build on existing work — must cite and clarify **weekend delta**
- Unfinished > no submission
- English preferred; Spanish/Portuguese accepted without penalty
- Written feedback not guaranteed for all projects

### Form fields to prepare before submitting
- Team name (or solo name)
- Emails
- Discord handles
- Project title
- Abstract
- PDF file

---

## Readings referenced (from page you pasted)

### All tracks
- Apart Research hackathon guide
- Concrete Problems in AI Safety (Amodei et al., 2016)
- BlueDot Impact courses
- Decolonial AI (Mohamed et al., 2020)
- Bridging the Multilingual Safety Divide (Banerjee et al., 2026)
- **Code-Switching Red-Teaming** (Yoo et al., ACL 2025) ← directly relevant to our project
- Soteria, MrGuard, CREST, Refusal Direction cross-lingual paper

### Asia-specific (used in our related work section)
- India AI Governance / Seven Sutras
- Vietnam AI Law (No. 134/2025/QH15, effective March 2026)
- ASEAN Guide on AI Governance
- **DECASTE** (IJCAI 2025) — caste bias ← our caste category inspiration
- **IndoSafety** (EMNLP 2025) — methodology template
- ThaiSafetyBench
- Deepfakes in India (WEF 2024)
- Small model jailbreak papers (ACL 2025)

### Tools listed on hackathon page
- DeepSafe Toolkit
- **Promptfoo** (we evaluated, chose not to use — see decision log)
- LightEval, PolyGuard, SALAD-Bench, HarmBench, ControlArena

### Adaption sponsor
- AutoScientist for training models
- Adaptive Data for datasets
- 300 Adaption credits included for participants
- **We did not use Adaption** — eval-only project, no fine-tuning

---

## Past Apart hackathon winners (pattern we designed for)

| Hackathon | Winner | Pattern |
|-----------|--------|---------|
| AI Manipulation (Jan 2026) | Who Does Your AI Serve? | Quantitative multi-model study, 3 experiments |
| AI Manipulation (Jan 2026) | Cross-Linguistic Sycophancy | **Multilingual benchmark — 3rd place** |
| Technical AI Governance (Feb 2026) | LidaSim | Novel methodology, policy simulation |
| AIxBio (Apr 2026) | Capiti | Focused eval with clear findings |

**Takeaway we applied:** Scoped experiment + numbers + clear PDF > ambitious unfinished system.

---

## Timeline constraints that shaped our project

When you started (June 20, 2026), roughly **~36 hours remained** until deadline.

This ruled out:
- Training models (Adaption/AutoScientist)
- Building new guardrail classifiers
- 120-seed benchmark at 60/language
- Multi-provider API comparison without keys
- Deepfake video pipelines

This favored:
- OpenAI-only eval
- 24 seeds (expandable later)
- Python pipeline runnable in one evening
- Report-first deliverable

---

## Asia track competition context

You compete **only against other Asia track submissions**, not Africa/LatAm.

Asia is described on the page as:
- Most dynamic AND most exposed region
- Half world's people, sharpest geopolitical fault lines
- Full spectrum of governance (India innovation-first, Vietnam binding AI law March 2026, ASEAN voluntary framework)

Our project addresses a gap explicitly listed: **safety evaluations for non-English / Indic language models**.

---

## Institutional contacts on page (for follow-up post-hackathon)

- Electric Sheep (Bengaluru)
- AI Safety India
- Secure AI Futures Lab (New Delhi)
- AI Safety Asia (pan-Asian network)
- Antoàn.ai (Vietnam)

Consider reaching out if project continues beyond hackathon.
