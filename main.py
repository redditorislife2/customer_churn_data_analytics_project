import argparse
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--data", type=Path, default=PROJECT_DIR / "customer_subscription_churn_usage_patterns.csv")
parser.add_argument("--output", type=Path, default=PROJECT_DIR / "outputs")
parser.add_argument("--no-show", action="store_true", help="Save plots without opening windows")
args = parser.parse_args()
if not args.data.is_file():
    parser.error(f"Dataset not found: {args.data}. Supply the original CSV with --data.")
if args.no_show:
    import matplotlib
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
args.output.mkdir(parents=True, exist_ok=True)
plot_number = 0

def save_plot(*unused_args, **unused_kwargs):
    global plot_number
    plot_number += 1
    plt.savefig(args.output / f"plot_{plot_number:02d}.png", bbox_inches="tight")
    plt.close()

if args.no_show:
    plt.show = save_plot

DATA_PATH = args.data
OUTPUT_DIR = args.output



# Run the original sections in order using shared script variables.
FILES = ['01_setup_and_cleaning.py', '02_features_and_churn_distribution.py', '03_kpis_and_distributions.py', '04_segment_analysis.py', '05_retention_and_correlations.py', '06_save_results.py']

for filename in FILES:
    path = PROJECT_DIR / filename
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), globals())
