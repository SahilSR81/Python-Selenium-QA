import os
from utils.failure_root_analyzer import FailureRootAnalyzer


def test_report_export():
    analyzer = FailureRootAnalyzer()
    analyzer.record_failure("test_b", "failure")
    path = analyzer.export_report()
    assert os.path.exists(path)
