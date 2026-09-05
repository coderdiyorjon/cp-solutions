"""
Binary Search Utilities using Python's bisect module.

The `bisect` module is implemented in C, making it significantly faster than 
manual while-loop implementation for list lookups.
"""

from bisect import bisect_left, bisect_right

def binary_search_exact(arr, target):
    """Finds the index of the first occurence of `target`.
    Returns:
        int: Index if found, otherwise -1.
    Time Complexity: O(log N)
    """
    idx = bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    return -1


def lower_bound(arr, target):
    """Finds the first index `i` such that `arr[i] >= target`.
    
    Equivalent to C++ std::lower_bound.

    Returns:
        int: Index in range [0, len(arr)]. Returns len(arr) if all elements < target.

    Time Complexity: O(log N)
    """

    return bisect_left(arr, target)


def upper_bound(arr, target):
    """Finds the first index `i` such that `arr[i] > target`.
    
    Equivalent to C++ std::upper_bound.
    
    Returns:
        int: Index in range [0, len(arr)]. Returns len(arr) if all elements <= target.
    
    Time Complexity: O(log N)
    """
    return bisect_right(arr, target)


def count_occurences(arr, target):
    """Counts the total occurences of `target` in a sorted array.
    
    Returns:
        int: Frequency of target.
    
    Time Complexity: O(log N)
    """
    return bisect_right(arr, target) - bisect_left(arr, target)


def find_predecessor(arr, target):
    """Finds largest element strictly smaller than `target`.
    
    Returns:
        int: Element if it exists, otherwise None.
        
    Time Complexity: O(log N)
    """
    idx = bisect_left(arr, target) - 1
    return arr[idx] if idx >= 0 else None


def find_successor(arr, target):
    """Finds the smallest element strictly greater than `target`.
    
    Returns:
        int: Element if it exists, otherwise None.
        
    Time Complexity: O(log N)
    """
    idx = bisect_right(arr, target)
    return arr[idx] if idx < len(arr) else None
