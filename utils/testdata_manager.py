import json
import os


class TestDataManager:

    @staticmethod
    def load(category, file_name):
        project_root = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(project_root, "testdata", category, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Test data file not found: {category}/{file_name}"
            )

        with open(file_path) as file:
            return json.load(file)
