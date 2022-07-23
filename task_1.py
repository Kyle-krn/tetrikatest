import json
from typing import List
from bs4 import BeautifulSoup
import requests
import random

def search_recursive(array: List, left: int = None, right: int = None) -> int:
    if isinstance(array, str):
        array = list(map(int, array))
    if left is None and right is None:
        left = -1
        right = len(array)
    if right - left <= 1:
        return right
    mid = (right + left) // 2
    if array[mid] == 0:
        right = mid
    else:
        left = mid
    return search_recursive(array, left, right)


def search(array: str) -> int:
    if isinstance(array, str):
        array = list(map(int, array))
    left = -1
    right = len(array)
    while right - left > 1:
        mid = (left + right) // 2
        if array[mid] == 0:
            right = mid
        else:
            left = mid
    return right
    
if __name__ == "__main__":
    for i in range(10):
        count_1 = random.randint(1, 50)
        string = ("1"*count_1) + ("0"*random.randint(1, 20))
        assert count_1 == search_recursive(string)
        assert count_1 == search(string)
        print("Done!")
        


