# Intuition

To guarantee exactly one valid path from the top-left to the bottom-right of a grid (assuming standard right and down movements), we must force the traveler into a single, inescapable corridor. The most straightforward shape for this corridor is an "L" or an inverted "L". By leaving the entire top row open and the entire rightmost column open, and blocking everything else, the only possible move sequence becomes: go all the way right, then go all the way down.

# Approach

We can construct this grid row by row:

1. **The First Row (Row 0):** This needs to be a completely clear path so we can travel all the way to the right edge. We fill it with `n` periods (`'.' * n`).
2. **The Remaining Rows (Rows 1 to m-1):** We want to block any downward movement before the rightmost edge. We fill the first `n - 1` cells with obstacles (`'#' * (n - 1)`) and leave only the last column open with a period (`'.'`).
3. We can wrap this logic in a single, clean Python list comprehension that iterates through the `m` rows.

# Complexity

* Time complexity:
$\mathcal{O}(m \times n)$
We are building $m$ strings, each of length $n$. String concatenation and replication in Python take time proportional to the length of the string produced.
* Space complexity:
$\mathcal{O}(m \times n)$
The space complexity is required to store the output list containing $m$ strings of length $n$. No additional auxiliary space is used.

# Code

```python []
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ['.' * n if not r
                else '#' * (n - 1) + '.'
                for r in range(m)
            ]
            
```
