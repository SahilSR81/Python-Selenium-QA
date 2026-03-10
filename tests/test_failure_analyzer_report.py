from utils.failure_root_analyzer import FailureRootAnalyzer

def test_report_generation():
    analyzer = FailureRootAnalyzer()
    analyzer.record_failure("test_a", "error")
    report = analyzer.generate_report()
    assert report["total_failures"] == 1
