# Intuition

Standard numeric parsers fail on "free-form" comma-separated input when whitespace appears *inside* a number (for example, between a sign and digits or between digits themselves). Because commas unambiguously separate values on each line, the problem reduces to splitting on `,`, stripping out all spaces from each token, and summing the parsed floating-point numbers line by line until EOF. [text](https://icpc.kattis.com/problems/freeforminput)

# Approach

1. **Stream Until EOF:** Iterate directly over `sys.stdin` to handle an arbitrary number of input lines without loading the entire input into memory at once.
2. **Skip Blank Lines:** Call `line.strip()` and skip empty lines so trailing newlines or blank separators don't trigger a `ValueError` during float conversion.
3. **Tokenize & Sanitize:** Split each line on `","` into raw number strings. For each token, call `part.replace(" ", "")` to remove both surrounding and internal spaces before converting with `float()`.
4. **Lazy Aggregation:** Wrap the conversion in a generator expression passed directly to `sum()`, avoiding an unnecessary intermediate list of floats, and print the total for each line.

# Complexity

* Time complexity:
$\mathcal{O}(L)$
Where $L$ is the total number of characters across the entire input. Each character is scanned a constant number of times during stripping, splitting, space removal, and float parsing.
* Space complexity:
$\mathcal{O}(K)$
Where $K$ is the length of the longest single line. Storing `parts` requires space proportional to the current line, while the generator expression streams floats into `sum()` in $\mathcal{O}(1)$ extra space.

# Code

```python
from sys import stdin

for line in stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(",")
    numbers = (float(part.replace(" ", "")) for part in parts)
    total = sum(numbers)
    print(total)

```
