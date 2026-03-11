import os


def test_suite_has_minimum_tests():
    tests = [f for f in os.listdir("tests") if f.startswith("test_")]
    assert len(tests) >= 20


def test_reports_directory_exists():
    assert os.path.isdir("reports")


def test_logs_directory_exists():
    assert os.path.isdir("logs")
