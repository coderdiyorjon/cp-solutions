# Intuition

To find the longest strictly increasing or decreasing subarray, we could write two separate loops—one checking if `num > prev` and another checking if `num < prev`. However, there is a much more elegant mathematical approach: a strictly decreasing sequence of numbers becomes a strictly increasing sequence if we simply multiply all the elements by $-1$. By leveraging this property, we only need to write the logic for an increasing sequence once.

# Approach

1. **Helper Function:** We define an inner function `increasing(nums)` that iterates through an array. It maintains a `length` counter that increments as long as the current number is strictly greater than the `prev` number. If the sequence breaks, `length` resets to 1. It constantly updates `longest` with the maximum length seen.
2. **Initial Run:** We pass the original `nums` array into `increasing()` to find the maximum strictly increasing subarray length.
3. **Negated Run:** We use a list comprehension `[-num for num in nums]` to invert the signs of all elements in the array. We pass this new array into `increasing()`, which effectively calculates the maximum strictly decreasing subarray length of the original array.
4. **Result:** We return the `max()` of these two calls.

# Complexity

* Time complexity:
$\mathcal{O}(N)$
Where $N$ is the length of the `nums` array. The `increasing()` function processes the array in a single linear pass ($\mathcal{O}(N)$). Creating the negated array via list comprehension takes another $\mathcal{O}(N)$. Running the function twice yields $\approx 3N$ operations, which strictly simplifies to $\mathcal{O}(N)$.
* Space complexity:
$\mathcal{O}(N)$
The auxiliary space complexity is dictated by the list comprehension `[-num for num in nums]`, which allocates a new array of size $N$ in memory. The helper function itself uses $\mathcal{O}(1)$ space for tracking variables.

# Code

```python3 []
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inf = float('inf')
        def increasing(nums: list[int]) -> int:
            length: int = 0
            longest: int = 0
            prev: float = inf

            for num in nums:
                if num > prev:
                    length += 1
                else:
                    length = 1
                prev = num
                longest = length if length > longest else longest
            
            return longest
        return max(increasing(nums), increasing([-num for num in nums]))

```