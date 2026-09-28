# 1614. Maximum Nesting Depth of the Parentheses

## Problem Overview

A string is a valid parentheses string (denoted VPS) if it meets standard bracket matching rules (e.g., `""`, `"" + "A"`, `"A" + "B"`, `"(A)"`).

You are given a VPS string `s`. Your task is to return the **nesting depth** of `s`. The nesting depth is essentially the maximum number of nested parentheses that are open at the exact same time.

---

## Examples

### Example 1
- **Input:** `s = "(1+(2*3)+((8)/4))+1"`
- **Output:** `3`
- **Explanation:** 
  The digit `8` is inside 3 nested parentheses: `(` ... `(` ... `(8)` ... `)` ... `)`.

### Example 2
- **Input:** `s = "(1)+((2))+(((3)))"`
- **Output:** `3`

---

## Constraints

- `1 <= s.length <= 100`
- `s` consists of digits `0-9` and characters `+`, `-`, `*`, `/`, `(`, and `)`.
- It is guaranteed that parentheses expression `s` is a Valid Parentheses String (VPS).

---

## Intuition & Approach

Think of the string as a building, and the parentheses are doors. 
- Every time you see an opening parenthesis `(`, you are walking one room deeper into the building. 
- Every time you see a closing parenthesis `)`, you are walking back out. 
- All other characters (numbers, math operators) are just furniture in the rooms—we can completely ignore them.

Since the problem guarantees the string is valid (no closing brackets without matching open ones), we don't even need a standard Stack data structure. We just need a simple counter.

1. Maintain a `count` variable to track our current depth.
2. Maintain a `Mx` variable to record the deepest we've ever gone.
3. Loop through the string: if we see `(`, increment `count` and update `Mx`. If we see `)`, decrement `count`.

---

## Solution Code

**File:** `0001.solution.py`

```python
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        Mx = count = 0
        
        for char in s:
            if char == '(':
                count += 1
                Mx = Mx if Mx > count else count
            elif char == ')':
                count -= 1
        
        return Mx