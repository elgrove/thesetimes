import logging
import sys


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    return logger
