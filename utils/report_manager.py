import os
import datetime


class ReportManager:

    @staticmethod
    def create_run_directory():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_dir = os.path.join(os.getcwd(), "reports", f"run_{timestamp}")
        screenshots_dir = os.path.join(base_dir, "screenshots")

        os.makedirs(screenshots_dir, exist_ok=True)

        return base_dir, screenshots_dir
