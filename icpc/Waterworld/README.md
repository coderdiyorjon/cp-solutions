# Intuition

At first glance, measuring water coverage on a rotating spherical planet sounds like it requires spherical integration or cosine weighting by latitude. However, the planet's image is sliced into $n$ horizontal bands of **equal height** and $m$ equal rotational steps.

By **Archimedes' Hat-Box Theorem**, the surface area of a spherical zone between two parallel planes depends only on the radius $R$ and the vertical height $h$ between the planes ($A = 2\pi R h$), not on latitude. Even though bands near the poles have a smaller circumference, the sphere's surface tilts more steeply there, compensating for the narrower radius. As a result, all $n \times m$ surface patches have the **exact same surface area**, so the overall water percentage is simply the unweighted arithmetic mean of all $n \times m$ cells.

# Approach

1. **Read Dimensions:** Parse $n$ (horizontal bands) and $m$ (rotational steps) from the first line.
2. **Accumulate Percentages:** Loop $n$ times, summing the $m$ integer percentages on each row directly into a running `total` without needing to store the 2D matrix in memory.
3. **Compute Mean:** Divide `total` by `m * n` and format the output to 10 decimal places (`:.10f`), safely clearing the judge's absolute error tolerance.

# Complexity

* Time complexity:
$\mathcal{O}(N \cdot M)$
Reads and sums every entry in the $N \times M$ grid exactly once. With $N, M \le 1000$, this processes at most $10^6$ integers.
* Space complexity:
$\mathcal{O}(M)$
Only a single row of $M$ integers is parsed at a time; the full grid is never stored.

# Code

```python
n, m = map(int, input().split())
total = 0
for i in range(n):
    total += sum(map(int, input().split()))
print(f"{total / (m * n):.10f}")

```
