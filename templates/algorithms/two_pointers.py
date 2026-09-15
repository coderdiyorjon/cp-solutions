"""Two pointers and Sliding Window Blueprints.
Common patterns:
1. Opposite ends (e.g., Two Sum on sorted array, Container With Most Water)
2. Dynamic Sliding Window (e.g., Longest/Shortest substring satisfying a condition)
3. Fixed-Size Sliding Window
"""

def two_pointers_opposite(arr, target):
    """Opposite ends pattern on a sorted array.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        return -1, -1
    
def sliding_window_variable(arr, condition_fn):
    """Dynamic-size sliding window(find maximum window satisfying condition).
    Time Complexity: O(N)
    Space Complexity: O(1) or O(K) depending on window state
    """
    left = 0
    best_len = 0
    window_state = {}
    
    for right in range(len(arr)):
        # 1. Expand: add arr[right] to window_state
        val = arr[right]
        window_state[val] = window_state.get(val, 0) + 1
        
        # 2. Shrink: while window violates the condition
        while not condition_fn(window_state):
            remove_val = arr[left]
            window_state[remove_val] -= 1
            if window_state[remove_val] == 0:
                del window_state[remove_val]
            left += 1
        
        # 3. Update answer with valid window
        best_len = max(best_len, right - left + 1)
    
    return best_len

def sliding_window(arr, k):
    """Fixed-size sliding window of length k.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if len(arr) < k:
        return 0
    
    # Initialize first window of size k.
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window one element at a time
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum