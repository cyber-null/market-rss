from config.env_config import LOG_LEVEL

import logging
import sys


def setup_logging():

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    conole_handler = logging.StreamHandler(sys.stdout)
    conole_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)
    
    if not root_logger.handlers:
        root_logger.addHandler(conole_handler)
