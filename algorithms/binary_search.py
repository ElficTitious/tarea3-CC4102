import numpy as np
from utilities.data_generation import *
import random as rand

def binary_search(arr, x):
    """Method that implements the algorithm binary search.
    If x is in arr, it returns the index where x is located in
    arr, otherwise it returns -1.

    Parameters
    ----------
    arr : [list] Sorted list of integers where to search for x.
    x : [int] Number that we want to search on arr.

    Returns
    -------
    [int] If x is in arr, then returns its position, otherwise, it
          returns.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if (arr[mid] == x):
            return mid
        if (x > arr[mid]):
            low = mid + 1
        else : high = mid - 1
    return -1  # If we reach this point it means x isnt in the array.

if __name__ == "__main__":
    
    even_num_arr = np.array([i for i in range(1000) if i % 2 == 0])
    for i in range(1000):
        if i % 2 == 0:
            assert(binary_search(even_num_arr, i) == i // 2)
        else:
            assert(binary_search(even_num_arr, i) == -1)
