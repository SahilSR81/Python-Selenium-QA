from utils.test_impact_analyzer import TestImpactAnalyzer


def test_detect_changed_files():
    analyzer = TestImpactAnalyzer()
    files = analyzer.detect_changed_files()
    assert isinstance(files, list)
