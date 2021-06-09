import logging
import sys


def create_logger():
    logger = logging.getLogger('server')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s %(funcName)s [%(username)s] -> %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
