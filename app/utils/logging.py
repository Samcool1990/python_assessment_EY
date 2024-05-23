import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_error(error: str):
    logger.error(error)
