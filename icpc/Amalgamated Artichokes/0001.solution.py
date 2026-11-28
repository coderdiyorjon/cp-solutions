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
