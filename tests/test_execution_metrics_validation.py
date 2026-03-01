import os
import json
import pytest


@pytest.mark.execution_order("last")
def test_execution_summary_generated():
    summary_path = os.path.join(os.getcwd(), "reports", "execution_summary.json")

    assert os.path.exists(summary_path), "Execution summary not generated"

    with open(summary_path) as f:
        data = json.load(f)

    assert "total_execution_time" in data
    assert "total_tests" in data
    assert isinstance(data["total_tests"], int)
