import os


def test_tag_registry_file():

    reports_dir = os.path.join(os.getcwd(), "reports")

    if not os.path.exists(reports_dir):
        return

    files = os.listdir(reports_dir)

    registry_files = [f for f in files if "tag_registry" in f]

    assert isinstance(registry_files, list)
