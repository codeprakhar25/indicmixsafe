"""Export case studies and human-validation sample for report writing."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import RESULTS_DIR, ensure_dirs


def export_drift_cases(df: pd.DataFrame, drift: pd.DataFrame, out_dir: Path) -> None:
    drift_only = drift[drift["drift"]].copy()
    rows = []
    for _, d in drift_only.iterrows():
        subset = df[(df["seed_id"] == d["seed_id"]) & (df["model_id"] == d["model_id"])]
        for _, r in subset.iterrows():
            rows.append(
                {
                    "seed_id": r["seed_id"],
                    "model_id": r["model_id"],
                    "category": r["category"],
                    "language": r["language"],
                    "variant": r["variant"],
                    "judge_label": r["judge_label"],
                    "prompt_preview": str(r["prompt_text"])[:120],
                    "response_preview": str(r["response_text"])[:200],
                }
            )
    out = pd.DataFrame(rows)
    out.to_csv(out_dir / "drift_case_studies.csv", index=False)
    print(f"Drift cases: {len(drift_only)} seed-model pairs -> {out_dir / 'drift_case_studies.csv'}")


def export_human_sample(df: pd.DataFrame, out_dir: Path, n: int = 30) -> None:
    sample_parts = []
    for category, group in df.groupby("category"):
        k = min(5, len(group))
        sample_parts.append(group.sample(k, random_state=42))
    sample = pd.concat(sample_parts).head(n)
    cols = [
        "prompt_id",
        "seed_id",
        "category",
        "variant",
        "language",
        "model_id",
        "judge_label",
        "prompt_text",
        "response_text",
    ]
    sample = sample[cols].copy()
    sample["human_label"] = ""
    sample["human_notes"] = ""
    sample.to_csv(out_dir / "human_validation_sample.csv", index=False)
    print(f"Human validation sample -> {out_dir / 'human_validation_sample.csv'} ({len(sample)} rows)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=RESULTS_DIR / "eval_results.csv")
    parser.add_argument("--output-dir", type=Path, default=RESULTS_DIR / "report_helpers")
    args = parser.parse_args()
    ensure_dirs()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.input)
    df = df[df["judge_label"] != "ERROR"]
    drift = pd.read_csv(RESULTS_DIR / "analysis" / "drift_per_seed.csv")

    export_drift_cases(df, drift, args.output_dir)
    export_human_sample(df, args.output_dir)

    top = drift[drift["drift"]].head(10)[["seed_id", "model_id", "category", "language", "labels"]]
    (args.output_dir / "top_drift_examples.json").write_text(
        top.to_json(orient="records", indent=2), encoding="utf-8"
    )
    print(f"Top drift JSON -> {args.output_dir / 'top_drift_examples.json'}")


if __name__ == "__main__":
    main()
