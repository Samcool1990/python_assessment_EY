from multiprocessing import Pool
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_lists(lists):
    try:
        return [sum(lst) for lst in lists]
    except Exception as e:
        logger.error(f"Error in addition: {e}")
        return None

def process_addition(lists):
    with Pool() as pool:
        results = pool.map(sum, lists)
    return results

def perform_addition(batchcid, payload):
    started_at = datetime.utcnow()
    try:
        response = process_addition(payload)
        status = "complete"
    except Exception as e:
        logger.error(f"Error processing batch {batchcid}: {e}")
        response = []
        status = "error"
    completed_at = datetime.utcnow()
    return {
        "batchcid": batchcid,
        "response": response,
        "status": status,
        "started_at": started_at,
        "completed_at": completed_at
    }
