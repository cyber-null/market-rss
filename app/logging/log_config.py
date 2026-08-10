import logging
import sys
import os

def setup_logging():
    level = os.getenv("LOG_LEVEL", "INFO").upper()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    conole_handler = logging.StreamHandler(sys.stdout)
    conole_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    if not root_logger.handlers:
        root_logger.addHandler(conole_handler)
