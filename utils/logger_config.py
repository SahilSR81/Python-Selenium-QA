import logging
import os
from datetime import datetime


def get_logger(name="framework_logger"):
    project_root = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(project_root, "logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(
        log_dir, f"test_run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    )

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
