import os
import json


def test_execution_metrics_structure():
    summary_path = os.path.join(os.getcwd(), "reports", "execution_summary.json")

    with open(summary_path) as f:
        data = json.load(f)

    assert isinstance(data["total_execution_time"], float)
    assert data["total_tests"] >= 1
    assert isinstance(data["slow_tests"], dict)
