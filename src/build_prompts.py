"""Expand seed CSVs (EN/MONO/CS/ROM columns) into long-format prompt table."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import DATA_DIR, ensure_dirs

VARIANTS = ["EN", "MONO", "CS", "ROM"]


def load_seeds(*paths: Path) -> pd.DataFrame:
    frames = [pd.read_csv(path) for path in paths]
    seeds = pd.concat(frames, ignore_index=True)
    required = {"seed_id", "language", "category", *VARIANTS}
    missing = required - set(seeds.columns)
    if missing:
        raise ValueError(f"Seed CSV missing columns: {sorted(missing)}")
    return seeds


def expand_variants(seeds: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for _, seed in seeds.iterrows():
        for variant in VARIANTS:
            rows.append(
                {
                    "prompt_id": f"{seed['seed_id']}_{variant}",
                    "seed_id": seed["seed_id"],
                    "language": seed["language"],
                    "category": seed["category"],
                    "variant": variant,
                    "text": seed[variant],
                    "is_harmful": seed["category"] != "benign_control",
                }
            )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build long-format prompt table from seeds.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DATA_DIR / "prompts_all.csv",
        help="Output CSV path",
    )
    args = parser.parse_args()
    ensure_dirs()

    seed_files = [DATA_DIR / "seeds_hindi.csv", DATA_DIR / "seeds_marathi.csv"]
    seeds = load_seeds(*seed_files)
    prompts = expand_variants(seeds)
    prompts.to_csv(args.output, index=False)

    print(f"Wrote {len(prompts)} prompts ({len(seeds)} seeds × {len(VARIANTS)} variants)")
    print(f"  Languages: {prompts['language'].value_counts().to_dict()}")
    print(f"  Categories: {prompts['category'].nunique()}")
    print(f"  Output: {args.output}")


if __name__ == "__main__":
    main()
