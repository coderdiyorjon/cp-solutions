def binary_search_exact(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements to search.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2 # Calculate the middle index

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1


def lower_bound(arr, target):
    """
    Finds the first index where arr[index] >= target.
    Returns len(arr) if no such element exists.
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than or equal to target, search in the left half
        if arr[mid] >= target:
            right = mid

        # If mid element is less than target, search in the right half
        else:
            left = mid + 1
    return left


def upper_bound(arr, target):
    """
    Finds the first index where arr[index] > target.
    Returns len(arr) if no such element exists.
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than target, search in the left half
        if arr[mid] > target:
            right = mid

        # If mid element is less than or equal to target, search in the right half
        else:
            left = mid + 1
    return left