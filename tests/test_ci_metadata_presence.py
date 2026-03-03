import os
import json


def test_summary_has_flaky_section():
    reports_root = os.path.join(os.getcwd(), "reports")
    run_dirs = sorted([d for d in os.listdir(reports_root) if d.startswith("run_")])

    if not run_dirs:
        return

    latest = run_dirs[-1]
    summary_path = os.path.join(reports_root, latest, "execution_summary.json")

    if not os.path.exists(summary_path):
        return

    with open(summary_path) as f:
        data = json.load(f)

    assert "flaky_tests" in data
