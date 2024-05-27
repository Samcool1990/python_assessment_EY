import multiprocessing
import logging
from typing import List

logger = logging.getLogger(__name__)

def add_lists(lists: List[List[int]]) -> List[int]:
    return [sum(lst) for lst in lists]

def addition_worker(payload: List[List[int]], return_dict):
    logger.info("Starting addition_worker")
    try:
        result = add_lists(payload)
        return_dict['result'] = result
    except Exception as e:
        logger.error(f"Error in addition_worker: {e}")
        return_dict['error'] = str(e)
    logger.info("Finished addition_worker")
