# app/views.py

from multiprocessing import Pool
from typing import List

def add_lists(lists: List[List[int]]) -> List[int]:
    return [sum(lst) for lst in lists]

def perform_addition(payload: List[List[int]]) -> List[int]:
    with Pool() as pool:
        result = pool.map(add_lists, [payload])
    return result[0]
