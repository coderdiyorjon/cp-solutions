# Intuition

Since the problem explicitly asks for the indices of the target *after* the array is sorted, the most logical first step is to sort the array. Once sorted, any duplicate occurrences of the target will be grouped together in a contiguous block. Instead of scanning the entire array from the beginning to find this block, we can use binary search to instantly locate the very first occurrence (the lower bound) of the target.

# Approach

1. **Sort:** First, sort the `nums` array in non-decreasing order.
2. **Binary Search (Lower Bound):** We set up a standard binary search using two pointers, `l` (left) and `r` (right). The condition `nums[mid] < target` ensures that if we see a number smaller than our target, we push the left boundary completely past it (`l = mid + 1`). If we see a number equal to or greater than the target, we bring the right boundary down (`r = mid`). This specific pattern guarantees that when the loop terminates (`l == r`), `l` will point to the **first** occurrence of the target (if it exists) or the insertion point where it should be.
3. **Collect Indices:** Starting from the found index `l`, we iterate forward. As long as the current number equals the target, we append its index to our result list. We stop as soon as we hit a larger number or reach the end of the array.

# Complexity

* Time complexity:
$O(N \log N)$
The dominant operation is the initial sorting of the array, which takes $O(N \log N)$ time. The binary search takes $O(\log N)$ time, and collecting the matching indices takes $O(K)$ time (where $K$ is the number of times the target appears). Overall, it simplifies to $O(N \log N)$.
* Space complexity:
$O(N)$
Python's built-in `sort()` (Timsort) requires $O(N)$ auxiliary space in the worst case. Additionally, the `ans` array will require $O(K)$ space to store the matching indices, which is bounded by $O(N)$.

# Code

```python []
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n: int = len(nums)
        l: int
        r: int
        l, r = 0, n

        while l < r:
            mid: int = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        ans: list[int] = []

        while l < n and nums[l] == target:
            ans.append(l)
            l += 1

        return ans
ns

```
