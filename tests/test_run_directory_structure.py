import os


def test_run_directory_created():
    reports_root = os.path.join(os.getcwd(), "reports")
    run_dirs = [d for d in os.listdir(reports_root) if d.startswith("run_")]

    assert len(run_dirs) > 0
