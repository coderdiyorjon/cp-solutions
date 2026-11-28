Given integer parameters $p, a, b, c, d$ and a sample count $n$, stock prices at time $k \in \{1, 2, \dots, n\}$ follow:

$$\text{price}(k) = p \cdot \bigl(\sin(a \cdot k + b) + \cos(c \cdot k + d) + 2\bigr)$$

Find the maximum price decline $\text{price}(i) - \text{price}(j)$ over all pairs $1 \le i \lt j \le n$, or `0.000000` if the price never decreases.
---

## Approach 1: Array-Based Running Maximum

### Intuition

For any point in time $j$, the largest possible decline ending at $j$ must start from the highest price observed at any earlier time $i \lt j$. Tracking a single running maximum as we scan left to right finds the worst drop in linear time without comparing all pairs. [Problem Source](https://icpc.kattis.com/problems/artichoke)

### Approach

1. **Parse Input:** Read `p, a, b, c, d, n`.
2. **Generate Price Series:** Precompute `prices[1..n]` using the given formula.
3. **Track Running Peak & Max Decline:** Initialize `mx = prices[1]` and `ret = 0.0`.
4. **Linear Scan:** For each price, update `mx` when a new peak appears; otherwise update `ret = max(ret, mx - prices[i])`.
5. **Output:** Print `ret` formatted to 6 decimal places.

### Complexity

* **Time complexity:** $\mathcal{O}(N)$ — two linear passes of length $N$ with $2N$ trigonometric evaluations.
* **Space complexity:** $\mathcal{O}(N)$ — stores the full `prices` array of length $N + 1$.

```python
from math import sin, cos

p, a, b, c, d, n = map(int, input().split())

prices = [0] * (n + 1)
for i in range(1, n + 1):
    prices[i] = p * (sin(a * i + b) + cos(c * i + d) + 2)

mx = prices[1]
ret = 0.0

for i in range(1, n + 1):
    if prices[i] > mx:
        mx = prices[i]
    else:
        ret = max(ret, mx - prices[i])

print(f"{ret:.6f}")

```

---

## Approach 2: $\mathcal{O}(1)$ Space Complex-Phasor Streaming

### Intuition

Two observations remove both the $\mathcal{O}(N)$ array and nearly all trigonometric calls:

1. **Algebraic simplification:** The constant $+2$ cancels out in $\text{price}(i) - \text{price}(j)$, and the positive multiplier $p$ factors out to the end:

$$\max_{i \lt j} \bigl(\text{price}(i) - \text{price}(j)\bigr) = p \cdot \max_{i \lt j} \bigl(f(i) - f(j)\bigr), \qquad f(k) = \sin(ak + b) + \cos(ck + d)$$


2. **Complex phasor recurrence:** By Euler's formula, advancing an angle by a fixed step is a single complex multiplication:

$$e^{i(a(k+1) + b)} = e^{i(ak + b)} \cdot e^{ia}$$



Python executes `z *= step` in C, giving $\sin(ak + b)$ as `z1.imag` and $\cos(ck + d)$ as `z2.real` without calling `sin()` or `cos()` inside the inner loop. [Problem Source](https://icpc.kattis.com/problems/artichoke)

### Approach

1. **Precompute Step Phasors:** Compute `step1 = complex(cos(a), sin(a))` and `step2 = complex(cos(c), sin(c))` once.
2. **Single-Pass Streaming:** Maintain only `mx` and `max_drop` inside `solve()` so loop variables stay in fast local slots.
3. **Chunked Re-Anchoring:** Recompute `z1` and `z2` directly every `10_000` iterations to prevent IEEE 754 floating-point drift from accumulating, keeping total error well below Kattis's $10^{-6}$ tolerance while reducing trig calls by $10{,}000\times$.
4. **Final Scaling:** Multiply `max_drop` by `p` once at the end and format to 6 decimal places.

### Complexity

* **Time complexity:** $\mathcal{O}(N)$ — single pass using C-level complex multiplications with only $\mathcal{O}(N / B)$ trig calls ($B = 10{,}000$).
* **Space complexity:** $\mathcal{O}(1)$ — uses only scalar and complex variables regardless of $N$.

```python
from math import sin, cos


def solve() -> None:
    p, a, b, c, d, n = map(int, input().split())

    step1 = complex(cos(a), sin(a))
    step2 = complex(cos(c), sin(c))

    mx = float("-inf")
    max_drop = 0.0

    block = 10_000
    for start in range(1, n + 1, block):
        z1 = complex(cos(a * start + b), sin(a * start + b))
        z2 = complex(cos(c * start + d), sin(c * start + d))
        end = min(start + block, n + 1)

        for _ in range(start, end):
            val = z1.imag + z2.real
            if val > mx:
                mx = val
            elif mx - val > max_drop:
                max_drop = mx - val
            z1 *= step1
            z2 *= step2

    print(f"{p * max_drop:.6f}")


if __name__ == "__main__":
    solve()

```

## Comparison

| Metric | `0001.solution.py` | `0002.solution.py` |
| --- | --- | --- |
| **Time Complexity** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Trig Calls ($N = 10^6$)** | $2{,}000{,}000$ | $\approx 404$ |
| **Key Technique** | Running-max array scan | Euler phasor recurrence + block re-anchoring |