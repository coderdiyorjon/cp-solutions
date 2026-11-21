# Intuition

As the introductory problem on ICPC/Kattis, this serves as a sanity check to verify that your submission workflow, Python interpreter version, and standard output (`stdout`) formatting work cleanly with the judge.

# Approach

Use Python's built-in `print()` function to output the exact string `'Hello World!'`. Online judges perform strict character-by-character comparisons, so matching the exact capitalization, spacing, and exclamation mark is all that is required.

# Complexity

* Time complexity:
$\mathcal{O}(1)$
Outputs a fixed, constant-length string of 12 characters.
* Space complexity:
$\mathcal{O}(1)$
Uses only a constant string literal with no auxiliary data structures.

# Code

```python
print('Hello World!')

```