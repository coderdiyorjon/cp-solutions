# 46. Permutations

## Problem Overview

**Platform:** LeetCode

**Problem ID:** 46

**Difficulty:** Medium

**Topics:** Array, Backtracking

You are given an array `nums` of distinct integers. Your task is to return all the possible permutations of those numbers. You can return the answer in any order.

A permutation is simply an arrangement of all the members of a set into some sequence or order.

---

## Examples

### Example 1:

* **Input:** `nums = [1, 2, 3]`
* **Output:** `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

### Example 2:

* **Input:** `nums = [0, 1]`
* **Output:** `[[0, 1], [1, 0]]`

### Example 3:

* **Input:** `nums = [1]`
* **Output:** `[[1]]`

---

## Constraints

* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
* All the integers of `nums` are **unique**.

---

## Intuition & Approach

Instead of relying on heavy combinatorics formulas, we can solve this by mimicking how we would construct these permutations logically by hand.

Imagine you have a handful of different colored blocks and you want to line them up in every possible order.

1. You pick one block to put in the first spot.
2. Then, from the remaining blocks, you pick another for the second spot.
3. You keep going until you run out of blocks.
4. Once you complete one full line, you write it down. Then, you take back the last block you placed and try a different one.

This process of building a solution step-by-step and "taking back" a choice to explore other options is called **backtracking**.

In the code:

* `ans` stores all our completed permutations.
* `sol` represents the current line of numbers we are building.
* We loop through the original `nums` array. If a number is not already in our current `sol`, we add it and call `backtrack()` to move to the next position.
* The base case for stopping is when `sol` reaches the same length as `nums`. At that point, we append a *copy* of `sol` (`sol[:]`) to our answers.
* Finally, `sol.pop()` removes the last number we added, allowing the loop to continue and try the next available number.

---

## Solution Code

**File:** `0001.solution.py`

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans, sol = [],  []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return ans

```

---

## Complexity Analysis

* **Time Complexity:** O(N × N!)
There are N! (N factorial) possible permutations. For each permutation, we take O(N) time to copy the current `sol` list into our `ans` array. The `num not in sol` check also takes linear time, but since N is very small (at most 6), this behaves effectively as constant time overhead.
* **Space Complexity:** O(N)
The recursion goes as deep as N layers. The `sol` array also takes O(N) space. This space complexity does not include the space required to hold the final output array.