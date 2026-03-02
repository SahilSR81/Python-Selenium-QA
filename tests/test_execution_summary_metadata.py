import os
import json


def test_summary_contains_metadata():
    reports_root = os.path.join(os.getcwd(), "reports")

    # ensure at least one run directory exists
    run_dirs = sorted([d for d in os.listdir(reports_root) if d.startswith("run_")])

    assert len(run_dirs) > 0, "No run directories found"

    latest = run_dirs[-1]
    summary_path = os.path.join(reports_root, latest, "execution_summary.json")

    # If summary not present yet, skip (session not finished yet)
    if not os.path.exists(summary_path):
        import pytest

        pytest.skip("Execution summary not generated yet")

    with open(summary_path) as f:
        data = json.load(f)

    assert "environment" in data
    assert "browser_mode" in data
