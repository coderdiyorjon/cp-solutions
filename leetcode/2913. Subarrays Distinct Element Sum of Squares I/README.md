# Intuition

To find the sum of squares of distinct element counts for all subarrays, the most straightforward approach is to generate every possible subarray, count its unique elements, square that count, and maintain a running total. Because a subarray is contiguous, we can efficiently build them by fixing a starting point and progressively expanding the endpoint to the right.

Alternatively, if we want to avoid recalculating from scratch, we can maintain the distinct counts dynamically. When extending our subarrays by adding a new element at index `i`, the distinct count only increases for subarrays starting *after* the last time we saw this element.

# Approach

### Solution 1: Running Set (Brute Force)

We use two nested loops. The outer loop `i` sets the starting index of the subarray. We initialize an empty `set` for each new starting point. The inner loop `j` iterates from `i` to the end of the array, expanding the subarray one element at a time. By adding `nums[j]` to our set, the size of the set automatically represents the number of distinct elements in the subarray `nums[i:j+1]`. We square this size and add it to `total_sum`.

### Solution 2: Dynamic Programming State

This approach calculates the answer incrementally by looking at all subarrays ending at index `i`.
Let `dp[j]` represent the number of distinct elements in the subarray `nums[j:i]`. When we move to `i+1`, the new element `nums[i]` only increases the distinct count for subarrays that start *after* its previous occurrence (`ls`).
Mathematically, if a subarray's distinct count increases from $x$ to $x+1$, its square increases by $(x+1)^2 - x^2 = 2x + 1$. We calculate this difference using the sum of our previous `dp` states (`2 * sum(dp[ls + 1:]) + (i - ls)`) and update the total and `dp` array for the next iteration.

# Complexity

### Solution 1

* Time complexity: $O(N^2)$
We have two nested loops iterating over the array of length $N$. Adding to a hash set and getting its length take $O(1)$ average time, making the total time proportional to the number of subarrays $\approx \frac{N^2}{2}$.
* Space complexity: $O(N)$
The set `distinct_elements` stores at most $N$ elements in the worst case (when all elements in the array are unique).

### Solution 2

* Time complexity: $O(N^2)$
Although it uses a DP approach, updating the `new_dp` array and calculating the `sum()` inside the loop takes $O(N)$ time per iteration over $N$ elements.
* Space complexity: $O(N)$
We store the `dp` array, `new_dp` array, and a hash map `last` to track the most recent index of each value. All of these require at most $O(N)$ space.

# Code

### Solution 1

```python3 []
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum: int
        total_sum = 0
        array_length: int
        array_length = len(nums)

        for i in range(array_length):
            distinct_elements: set[int]
            distinct_elements = set()
            
            for j in range(i, array_length):
                distinct_elements.add(nums[j])
                
                distinct_counts: int
                distinct_counts = len(distinct_elements)
                
                total_sum += distinct_counts ** 2
            
        return total_sum

```

### Solution 2

```python3 []
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 1
        prev = 1
        dp = [1]
        last = {}
        last[nums[0]] = 0
        for i in range(1, len(nums)):
            new_dp = [0] * (i + 1)
            ls = last[nums[i]] if nums[i] in last else -1
            cur = prev + 2 * (sum(dp[ls + 1:])) + i - ls
            ans += cur
            for j in range(ls + 1):
                new_dp[j] = dp[j]
            for j in range(ls + 1, i):
                new_dp[j] = dp[j] + 1
            new_dp[-1] = 1

            prev = cur
            dp = new_dp
            last[nums[i]] = i
        return ans

```