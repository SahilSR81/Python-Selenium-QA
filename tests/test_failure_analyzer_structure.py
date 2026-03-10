from utils.failure_root_analyzer import FailureRootAnalyzer


def test_failure_structure():
    analyzer = FailureRootAnalyzer()
    analyzer.record_failure("test_login", "element not found")
    report = analyzer.generate_report()
    assert "failures" in report
