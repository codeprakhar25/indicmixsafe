# IndicMixSafe — Report Outline (paste into Apart submission template)

## Title
IndicMixSafe: Code-Switching Safety Failures in Hindi and Marathi LLM Interactions

## Abstract (≤150 words)
[TBD after results — template:]
Large language models deployed in India face prompts in Hinglish, Romanized Hindi, and Marathi-English code-switch — registers absent from English-centric safety benchmarks. We evaluate OpenAI models (GPT-4o, GPT-4.1-mini, GPT-4o-mini) on N culturally grounded prompts across six harm categories, each expressed in four variants: English, monolingual Indic, code-switched, and Romanized script. We find [X]% higher attack success rate in code-switched/Romanized variants vs English for caste, religion, and political misinformation categories, with significant cross-variant safety drift. We release prompt templates and evaluation scripts to support language-aware alignment for Indic deployments.

**Track:** Asia · Technical Safety (Socio-economic: caste, misinformation)

**Authors:** [Your name, affiliation]

---

## 1. Introduction
- India: 1.2B+ speakers, dominant online register is code-mixed (Hinglish, Romanized Devanagari)
- Safety alignment trained on clean English + formal Hindi fails silently on real user prompts
- **Research question:** Do models refuse harmful requests consistently across EN / MONO / CS / ROM?
- **Contribution this weekend:** First systematic Hinglish + Marathi code-switch safety eval with drift metrics

## 2. Related Work
- CSRT (Yoo et al., ACL 2025): code-switching red-teaming, +46.7% ASR vs English
- DECASTE (IJCAI 2025): caste bias in LLMs
- IndicSafe (2026): unreleased; motivates our open mini-benchmark
- IndoSafety (EMNLP 2025): methodology template for culturally grounded safety eval

## 3. Methodology

### 3.1 Prompt construction
- 60 Hindi + 60 Marathi seeds (6 categories × 10)
- 4 variants per seed: EN, MONO, CS, ROM
- Categories: caste, religion, political_misinfo, gender_harm, general_violence, benign_control

### 3.2 Models
- gpt-4o, gpt-4.1-mini, gpt-4o-mini (OpenAI API)

### 3.3 Evaluation
- LLM-as-judge (gpt-4o-mini): REFUSE / COMPLY / AMBIGUOUS
- Human validation: 30 samples, report Cohen's κ or agreement %

### 3.4 Metrics
- **ASR:** COMPLY rate on harmful prompts (REFUSE rate on benign = over-refusal)
- **Safety drift:** same seed+model, different label across variants
- **Category breakdown:** caste vs general_violence gap

## 4. Results
- Table 1: ASR by model × variant (from `asr_by_variant_model.csv`)
- Table 2: ASR by category × variant (from `asr_by_category_variant.csv`)
- Figure 1: Bar chart — EN vs CS vs ROM mean ASR for India-specific categories
- Key finding 1: [fill after run]
- Key finding 2: [fill after run]
- Case study: 1 seed where EN=REFUSE but CS=COMPLY (paraphrase, don't paste full harmful text)

## 5. Discussion
- Implications for Bhashini, Sarvam, WhatsApp AI, UPI chatbots
- Code-mix and Romanized script should be in safety training data
- Romanization as evasion vector (users avoid script-based filters)
- Comparison to CSRT global findings

## 6. Limitations and Dual-Use Considerations
- Small prompt set (N=120 seeds); not exhaustive of Indic harms
- OpenAI models only; no Sarvam/Krutrim comparison
- LLM judge bias; mitigated by human spot-check
- Dual-use: prompt templates could aid misuse → we release structure not raw harmful outputs
- Marathi variants not native-reviewed [if applicable]
- Future: Gujarati/Kannada extension, open-weight models, guardrail fine-tuning

## 7. What's New This Weekend
- [ ] Curated Hinglish + Marathi code-switch safety prompt set
- [ ] Quantified cross-variant safety drift on India-specific harm categories
- [ ] Open evaluation pipeline (Python, reproducible)
- [ ] [Add after run] First measurement of ASR gap between EN and CS/ROM for caste/religion prompts

## References
- Yoo et al. (2025). Code-Switching Red-Teaming. ACL.
- [DECASTE, IndicSafe, IndoSafety, HarmBench, etc.]
