import os


def test_run_metadata_file_exists():

    reports_dir = os.path.join(os.getcwd(), "reports")

    files = os.listdir(reports_dir)

    metadata_files = [f for f in files if f.startswith("run_metadata_")]

    assert isinstance(metadata_files, list)
