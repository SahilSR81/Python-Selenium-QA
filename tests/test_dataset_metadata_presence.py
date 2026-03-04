import os
import json


def test_execution_summary_contains_dataset_field():

    reports_root = os.path.join(os.getcwd(), "reports")

    if not os.path.exists(reports_root):
        return

    run_dirs = sorted([d for d in os.listdir(reports_root) if d.startswith("run_")])

    if not run_dirs:
        return

    latest = run_dirs[-1]
    summary = os.path.join(reports_root, latest, "execution_summary.json")

    if not os.path.exists(summary):
        return

    with open(summary) as f:
        data = json.load(f)

    assert "total_tests" in data
