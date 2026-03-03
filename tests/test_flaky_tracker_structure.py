from utils.flaky_tracker import FlakyTracker


def test_flaky_tracker_basic():
    tracker = FlakyTracker()
    tracker.record_retry("test_sample")
    result = tracker.get_flaky_tests()

    assert "test_sample" in result
    assert result["test_sample"] == 1
