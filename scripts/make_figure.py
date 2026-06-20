"""Generate Figure 1 for the report PDF.

Figure 1 contrasts the *automated LLM-judge* ASR against the *author-audited
strict* ASR for the two India-specific harm categories (caste, electoral
misinformation). It visualizes the paper's second contribution: the judge
over-counts attack success on Indic prompts, and the caste signal collapses
under audit while the electoral-misinformation signal largely survives.

All numbers are computed from raw artifacts (no hardcoded ASR):
  - results/eval_results.csv                          -> judge COMPLY counts
  - results/report_helpers/harmful_comply_audit.csv   -> audit downgrades
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from config_loader import RESULTS_DIR, ensure_dirs

FOCUS_CATEGORIES = ["caste", "political_misinfo"]
VARIANT_ORDER = ["EN", "MONO", "CS", "ROM"]


def _truthy(series: pd.Series) -> pd.Series:
    """Coerce is_harmful column (bool or 'True'/'False' strings) to bool."""
    if series.dtype == bool:
        return series
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def compute_asr() -> pd.DataFrame:
    """Return per category x variant judge vs audited ASR (%)."""
    eval_df = pd.read_csv(RESULTS_DIR / "eval_results.csv")
    eval_df = eval_df[_truthy(eval_df["is_harmful"])].copy()

    audit = pd.read_csv(RESULTS_DIR / "report_helpers" / "harmful_comply_audit.csv")
    # A downgrade = judge said COMPLY but audit said it was NOT genuine compliance.
    downgrades = audit[audit["human"].str.upper() != "COMPLY"]
    downgrade_keys = set(
        zip(downgrades["seed_id"], downgrades["model"], downgrades["variant"])
    )

    eval_df["is_comply"] = eval_df["judge_label"].str.upper() == "COMPLY"
    eval_df["is_downgrade"] = [
        (s, m, v) in downgrade_keys
        for s, m, v in zip(
            eval_df["seed_id"], eval_df["model_id"], eval_df["variant"]
        )
    ]
    # Audited compliance = judge COMPLY that survived the audit.
    eval_df["is_confirmed"] = eval_df["is_comply"] & ~eval_df["is_downgrade"]

    grp = (
        eval_df.groupby(["category", "variant"])
        .agg(n=("is_comply", "size"),
             judge=("is_comply", "sum"),
             audited=("is_confirmed", "sum"))
        .reset_index()
    )
    grp["judge_pct"] = 100.0 * grp["judge"] / grp["n"]
    grp["audited_pct"] = 100.0 * grp["audited"] / grp["n"]
    return grp


def main() -> None:
    ensure_dirs()
    grp = compute_asr()

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
    x = np.arange(len(VARIANT_ORDER))
    width = 0.38

    for ax, category in zip(axes, FOCUS_CATEGORIES):
        sub = (
            grp[grp["category"] == category]
            .set_index("variant")
            .reindex(VARIANT_ORDER)
            .fillna(0.0)
        )
        b1 = ax.bar(x - width / 2, sub["judge_pct"], width,
                    label="Automated judge", color="#e74c3c",
                    edgecolor="black", linewidth=0.5)
        b2 = ax.bar(x + width / 2, sub["audited_pct"], width,
                    label="Author-audited (strict)", color="#2c7fb8",
                    edgecolor="black", linewidth=0.5)

        ax.set_title(category.replace("_", " ").title())
        ax.set_xlabel("Language register")
        ax.set_xticks(x)
        ax.set_xticklabels(VARIANT_ORDER)
        ax.set_ylim(0, 40)
        for bars in (b1, b2):
            for bar in bars:
                h = bar.get_height()
                if h > 0:
                    ax.text(bar.get_x() + bar.get_width() / 2, h + 0.8,
                            f"{h:.1f}", ha="center", fontsize=8)

    axes[0].set_ylabel("Attack Success Rate (%)")
    axes[1].legend(fontsize=9, loc="upper left")
    fig.suptitle(
        "Judge vs. audited ASR by register "
        "(caste collapses under audit, electoral misinfo survives)",
        fontsize=11,
    )
    fig.tight_layout()

    out = RESULTS_DIR / "analysis" / "figure1_judge_vs_audited.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
