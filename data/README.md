# Data

This directory holds the harm-scenario seed prompts and the generated prompt set:

- `seeds_hindi.csv`: 12 Hindi seeds (2 per category)
- `seeds_marathi.csv`: 12 Marathi seeds (2 per category)
- `prompts_all.csv`: 96 generated prompt variants (4 registers x 24 seeds)

These CSVs are intentionally excluded from the public repository (see the project
`.gitignore`). They contain verbatim harmful prompts across caste, religion,
electoral misinformation, gender, and violence categories, which is dual-use
material that should not be redistributed without access controls.

The full evaluation outputs (`results/eval_results.csv`) are also withheld, since
they contain raw model responses to those prompts.

For reproducibility, the seeds and full results are available to hackathon
organizers, reviewers, and researchers on request. The pipeline (`src/`,
`scripts/`) regenerates all analysis artifacts from the seed CSVs.
Contact: prakhar@agentdiff.site.
