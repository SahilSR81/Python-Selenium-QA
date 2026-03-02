import os
from datetime import datetime


def capture_screenshot(driver, test_name):
    # ---- Try to detect latest run folder ----
    reports_root = os.path.join(os.getcwd(), "reports")

    if not os.path.exists(reports_root):
        os.makedirs(reports_root, exist_ok=True)

    # Find latest run directory
    run_dirs = [d for d in os.listdir(reports_root) if d.startswith("run_")]

    if run_dirs:
        latest_run = sorted(run_dirs)[-1]
        screenshots_dir = os.path.join(reports_root, latest_run, "screenshots")
    else:
        # fallback (old behavior)
        screenshots_dir = os.path.join(reports_root, "screenshots")

    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{test_name}_{timestamp}.png"
    file_path = os.path.join(screenshots_dir, file_name)

    driver.save_screenshot(file_path)
    return file_path
