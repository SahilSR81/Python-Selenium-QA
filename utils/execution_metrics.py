import time
import json
import os
from utils.report_manager import ReportManager


class ExecutionMetrics:
    def __init__(self):
        self.start_time = time.time()
        self.test_durations = {}

        # ---- NEW: Timestamped Run Directory ----
        self.base_dir, self.screenshots_dir = ReportManager.create_run_directory()

        # Old behavior preserved (still writes summary file)
        self.report_path = os.path.join(self.base_dir, "execution_summary.json")

    def record_test(self, test_name, duration):
        self.test_durations[test_name] = duration

    def generate_summary(self, env=None, browser_mode=None):
        total_time = time.time() - self.start_time

        slow_tests = {
            name: round(dur, 2) for name, dur in self.test_durations.items() if dur > 2
        }

        return {
            "total_execution_time": round(total_time, 2),
            "total_tests": len(self.test_durations),
            "slow_tests": slow_tests,
            # ---- NEW METADATA ----
            "environment": env,
            "browser_mode": browser_mode,
        }

    def export_summary(self, summary):
        os.makedirs(self.base_dir, exist_ok=True)

        with open(self.report_path, "w") as f:
            json.dump(summary, f, indent=4)

        return self.report_path
