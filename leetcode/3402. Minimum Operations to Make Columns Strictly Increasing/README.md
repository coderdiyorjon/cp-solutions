# 3402. Minimum Operations to Make Columns Strictly Increasing

## Problem Overview

You are given a $m \times n$ matrix `grid` consisting of non-negative integers. In one operation, you can increment the value of any `grid[i][j]` by 1. 

Your task is to return the minimum number of operations needed to make all columns of `grid` strictly increasing.

---

## Examples

### Example 1
**Input:** `grid = [[3,2],[1,3],[3,4],[0,1]]`
**Output:** `15`
**Explanation:** 
* To make the 0th column strictly increasing, we can apply 3 operations on `grid[1][0]`, 2 operations on `grid[2][0]`, and 6 operations on `grid[3][0]`.
* To make the 1st column strictly increasing, we can apply 4 operations on `grid[3][1]`.
* Total operations: 3 + 2 + 6 + 4 = 15.

### Example 2
**Input:** `grid = [[3,2,1],[2,1,0],[1,2,3]]`
**Output:** `12`

---

## Constraints

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 50`
* `0 <= grid[i][j] < 2500`

---

## Intuition & Approach

Because operations applied to one column do not affect the elements of another column, we can solve this greedily by evaluating each column completely independently. 

For a column to be **strictly increasing**, every element `grid[i+1][j]` must be strictly greater than the element directly above it, `grid[i][j]`. The absolute minimum value `grid[i+1][j]` can take to satisfy this condition without overspending operations is exactly `grid[i][j] + 1`.

### The Strategy:
1. Traverse the matrix column by column.
2. For each column, iterate downwards row by row.
3. If we find that `grid[i][j] >= grid[i+1][j]`, we have found a sequence violation.
4. Calculate the required target value for the lower cell: `target = grid[i][j] + 1`.
5. Add the required number of increments (`target - grid[i+1][j]`) to a running total `oper_count`.
6. Update the lower cell to `target` so subsequent rows in the column can be correctly evaluated against this new baseline.

---

## Solution Code

**File:** `0001.solution.py`

```python
from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        oper_count = 0
        
        # Traverse column by column
        for j in range(len(grid[0])):
            # Traverse downwards within the column
            for i in range(len(grid) - 1):
                # Check if the strictly increasing condition is violated
                if grid[i][j] >= grid[i + 1][j]:
                    target = grid[i][j] + 1
                    oper_count += target - grid[i + 1][j]
                    
                    # Update the cell to maintain the baseline for the next row
                    grid[i + 1][j] = target
                    
        return oper_count
