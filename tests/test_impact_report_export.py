import os
from utils.test_impact_analyzer import TestImpactAnalyzer


def test_export_report():
    analyzer = TestImpactAnalyzer()
    analyzer.changed_files = ["sample.py"]
    analyzer.affected_tests = ["tests/test_sample.py"]
    path = analyzer.export_report()
    assert os.path.exists(path)
