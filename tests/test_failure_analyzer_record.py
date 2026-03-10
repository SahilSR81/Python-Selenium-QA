from utils.failure_root_analyzer import FailureRootAnalyzer

def test_failure_record():
    analyzer = FailureRootAnalyzer()
    analyzer.record_failure("test_sample", "Sample error")
    assert len(analyzer.failures) == 1
