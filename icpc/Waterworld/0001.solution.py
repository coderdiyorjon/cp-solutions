n, m = map(int, input().split())
total = 0
for i in range(n):
    total += sum(map(int, input().split()))
print(f"{total / (m * n):.10f}")
