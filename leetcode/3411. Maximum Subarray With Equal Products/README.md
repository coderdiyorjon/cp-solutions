# 3411. Maximum Subarray With Equal Products

## Problem Overview

**Platform:** LeetCode

**Problem ID:** 3411

**Difficulty:** Easy

**Topics:** Array, Math, Number Theory, Sliding Window

Given an array of positive integers `nums` (with $2 \le \text{len}(\text{nums}) \le 100$ and $1 \le \text{nums}[i] \le 10$), find the length of the longest contiguous subarray where $\text{prod}(\text{arr}) = \text{lcm}(\text{arr}) \times \text{gcd}(\text{arr})$.

---

## Approach 1: Incremental Subarray Enumeration (`0001.solution.py`)

### Intuition

With $N \le 100$, checking every contiguous subarray directly is fast enough. Instead of recomputing the product, LCM, and GCD from scratch for each subarray, we can fix a starting index `i` and update all three running values incrementally as we extend the right endpoint `j`.

### Approach

1. Loop `i` from `0` to `n - 1` as the left boundary of the subarray.
2. Initialize identity elements for the running operations: `prod = 1`, `l = 1` (since $\text{lcm}(1, x) = x$), and `g = 0` (since $\text{gcd}(0, x) = x$).
3. Extend `j` from `i` to `n - 1`, updating `prod *= nums[j]`, `l = math.lcm(l, nums[j])`, and `g = math.gcd(g, nums[j])`.
4. Whenever `prod == l * g`, update `ans` with `max(ans, j - i + 1)`.

### Complexity

* **Time complexity:** $\mathcal{O}(N^2 \log M)$, where $M = \max(\text{nums})$. The nested loops inspect $\mathcal{O}(N^2)$ subarrays, and each `math.gcd` / `math.lcm` call takes $\mathcal{O}(\log M)$ time. (Note: in Python, `prod` grows exponentially up to $10^{100}$, so arbitrary-precision multiplication adds a small factor on large subarrays, though $N \le 100$ keeps it negligible.)
* **Space complexity:** $\mathcal{O}(1)$ auxiliary space (ignoring the big-integer bit length of `prod`).

### Code (`0001.solution.py`)

```python
import math


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            l = 1
            g = 0
            for j in range(i, n):
                prod *= nums[j]
                l = math.lcm(l, nums[j])
                g = math.gcd(g, nums[j])
                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans

```

---

## Approach 2: Prime Factorization & Coprime Sliding Window (`0002.solution.py`)

### Intuition

Look at the exponent $e_1, e_2, \dots, e_k \ge 0$ of any single prime $p$ across a subarray of length $k$:

* In $\text{prod}$, the exponent of $p$ is $\sum_{i=1}^{k} e_i$.
* In $\text{lcm} \times \text{gcd}$, the exponent of $p$ is $\max_i e_i + \min_i e_i$.

This gives two immediate rules:

1. **Length 2 always works:** For $k = 2$, $e_1 + e_2 = \max(e_1, e_2) + \min(e_1, e_2)$ holds unconditionally for every prime. So any array of length at least 2 has an answer of at least `2`.
2. **Length 3 or more requires pairwise coprimality:** For $k \ge 3$, $\sum e_i = \max e_i + \min e_i$ forces all $k - 2$ middle exponents to be $0$, which in turn forces $\min e_i = 0$. Therefore, **at most one** element in the subarray can be divisible by $p$ — no two elements may share any prime factor.

Because $1 \le \text{nums}[i] \le 10$, the only possible prime factors are `2, 3, 5, 7`, which makes tracking shared primes with a sliding window effortless.

### Approach

1. **Precomputed Prime Table:** Store the distinct prime factors for each integer `0..10` in a lookup tuple `PRIMES` (note that `1` has no prime factors, so `1` is coprime with everything and never invalidates a window).
2. **Initialize Baseline:** Set `res = min(len(nums), 2)` to cover the guaranteed length-2 case. Maintain `last_seen` (size 8, indexed directly by primes `2, 3, 5, 7`) initialized to `-1`, and a left pointer `start = 0`.
3. **Slide the Window:** As `end` scans through `nums`, check every prime factor `p` of `x = nums[end]`. If `last_seen[p] >= start`, a duplicate prime exists inside the current window, so jump `start` to `last_seen[p] + 1` to evict the conflicting element. Update `last_seen[p] = end`.
4. **Track Maximum:** Update `res` with `end - start + 1` at each step.

### Complexity

* **Time complexity:** $\mathcal{O}(N)$. Each element is visited once, and since every number up to 10 has at most 2 distinct prime factors, the inner loop does $\mathcal{O}(1)$ work per element.
* **Space complexity:** $\mathcal{O}(1)$. Both `PRIMES` and `last_seen` are fixed-size structures independent of $N$.

### Code (`0002.solution.py`)

```python
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        # Prime factors for each number from 0 to 10
        PRIMES = (
            (),      # 0 (unused)
            (),      # 1 (no prime factors)
            (2,),    # 2
            (3,),    # 3
            (2,),    # 4
            (5,),    # 5
            (2, 3),  # 6
            (7,),    # 7
            (2,),    # 8
            (3,),    # 9
            (2, 5),  # 10
        )

        last_seen = [-1] * 8
        res = min(len(nums), 2)
        start = 0

        for end, x in enumerate(nums):
            for p in PRIMES[x]:
                if last_seen[p] >= start:
                    start = last_seen[p] + 1
                last_seen[p] = end

            curr_len = end - start + 1
            if curr_len > res:
                res = curr_len

        return res

```
