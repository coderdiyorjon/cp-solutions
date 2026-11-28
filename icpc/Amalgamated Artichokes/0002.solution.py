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