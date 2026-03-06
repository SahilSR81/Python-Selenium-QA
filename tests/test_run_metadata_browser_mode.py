import os
import json


def test_run_metadata_browser_mode():

    reports_dir = os.path.join(os.getcwd(), "reports")

    files = [f for f in os.listdir(reports_dir) if f.startswith("run_metadata_")]

    if not files:
        return

    latest = sorted(files)[-1]

    path = os.path.join(reports_dir, latest)

    with open(path) as f:
        data = json.load(f)

    assert "browser_mode" in data
