from multiprocessing import Pool
from typing import List

def add_lists(input_list: List[int]) -> int:
    return sum(input_list)

def perform_addition(payload: List[List[int]]) -> List[int]:
    with Pool(processes=4) as pool:
        results = pool.map(add_lists, payload)
    return results
