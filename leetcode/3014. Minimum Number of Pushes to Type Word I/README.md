# 3014. Minimum Number of Pushes to Type Word I

## Problem Overview

**Platform:** LeetCode
**Problem ID:** 3014
**Difficulty:** Easy
**Topics:** Math, String, Greedy

You are given a string `word` consisting of **distinct lowercase English letters**.

A telephone keypad contains 8 usable keys (`2` through `9`). Each key can be mapped to any number of distinct letters, and each letter can be assigned to at most one key.

Your task is to remap the letters to the keypad so that the total number of key presses required to type `word` is minimized.

Return the minimum number of pushes needed to type the given word.

> **Note**
>
> Keys `1`, `*`, `#`, and `0` do not contain any letters.

---

## Examples

### Example 1

**Input**

```text
word = "abcde"
```

**Output**

```text
5
```

**Explanation**

Assign each character as the first letter of a different key:

* `a` → key `2`
* `b` → key `3`
* `c` → key `4`
* `d` → key `5`
* `e` → key `6`

Each character requires exactly one push.

Total pushes:

```text
1 + 1 + 1 + 1 + 1 = 5
```

---

### Example 2

**Input**

```text
word = "xycdefghij"
```

**Output**

```text
12
```

**Explanation**

* The first 8 letters can be assigned as the first character on each key.

  * Cost: `8 × 1 = 8`
* The remaining 2 letters become second-position characters.

  * Cost: `2 × 2 = 4`

Total pushes:

```text
8 + 4 = 12
```

---

## Constraints

* `1 <= word.length <= 26`
* `word` contains only lowercase English letters.
* All characters in `word` are distinct.

---

## Intuition

There are only **8 available keys** (`2` through `9`).

To minimize the total number of pushes:

* The first 8 letters should occupy the first position on each key.
* The next 8 letters should occupy the second position.
* The next 8 letters should occupy the third position.
* Any remaining letters occupy the fourth position.

Since every character appears exactly once and all characters are distinct, the actual character values do not matter. Only the number of characters matters.

Therefore, characters can be grouped in batches of 8:

| Character Group   | Push Cost |
| ----------------- | --------- |
| 1st 8 letters     | 1         |
| 2nd 8 letters     | 2         |
| 3rd 8 letters     | 3         |
| Remaining letters | 4         |

---

## Solution 1: Group-Based Simulation

**File:** `0001.solution.py`

### Idea

Process the word length in groups of 8 characters.

For each group:

1. Calculate how many characters belong to the current group.
2. Multiply that amount by the current push cost.
3. Increase the push cost for the next group.

### Implementation

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Total number of characters
        n = len(word)

        # Current push cost
        cost = 1

        # Total pushes required
        pushes = 0

        # Process characters in groups of 8
        while n:
            if n > 8:
                pushes += 8 * cost
                n -= 8
            else:
                pushes += n * cost
                n = 0

            cost += 1

        return pushes
```

### Complexity Analysis

* Time Complexity: `O(1)`
* Space Complexity: `O(1)`

Although the loop appears iterative, the maximum word length is only 26, so at most four groups are processed.

---

## Solution 2: Mathematical Observation

**File:** `0002.solution.py`

### Idea

Each character belongs to a group of size 8.

For a character at index `i`:

```text
0-7   -> 1 push
8-15  -> 2 pushes
16-23 -> 3 pushes
24-31 -> 4 pushes
```

The push cost can be calculated directly as:

```text
(i // 8) + 1
```

Summing this value for every index gives the answer.

### Implementation

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        return sum((i // 8 + 1) for i in range(n))
```

### Complexity Analysis

* Time Complexity: `O(N)`
* Space Complexity: `O(1)`

where `N` is the length of `word`.

---

## Complexity Comparison

| Solution               | Time Complexity | Space Complexity |
| ---------------------- | --------------- | ---------------- |
| Group-Based Simulation | O(1)            | O(1)             |
| Mathematical Generator | O(N)            | O(1)             |

> Since `N <= 26`, both solutions run in effectively constant time for all valid inputs.

---

## Key Takeaway

The important observation is that there are only **8 usable keypad keys**.

To minimize total pushes, assign characters to keypad positions in increasing order of cost:

* First 8 characters → cost 1
* Next 8 characters → cost 2
* Next 8 characters → cost 3
* Remaining characters → cost 4

Once this pattern is recognized, the solution becomes a straightforward counting problem.
