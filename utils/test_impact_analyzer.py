import subprocess
import os
import json


class TestImpactAnalyzer:

    def __init__(self):
        self.changed_files = []
        self.affected_tests = []

    def detect_changed_files(self):
        try:
            result = subprocess.check_output(
                ["git", "diff", "--name-only", "HEAD~1", "HEAD"], text=True
            )
            self.changed_files = [f.strip() for f in result.split("\n") if f.strip()]
        except Exception:
            self.changed_files = []

        return self.changed_files

    def map_tests(self, tests_dir="tests"):

        if not self.changed_files:
            return []

        for root, _, files in os.walk(tests_dir):

            for file in files:

                if not file.startswith("test_"):
                    continue

                file_path = os.path.join(root, file)

                for changed in self.changed_files:

                    if changed.split("/")[-1] in file:
                        self.affected_tests.append(file_path)

        return list(set(self.affected_tests))

    def export_report(self):

        report = {
            "changed_files": self.changed_files,
            "affected_tests": self.affected_tests,
        }

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        path = os.path.join(reports_dir, "impact_analysis.json")

        with open(path, "w") as f:
            json.dump(report, f, indent=4)

        return path
