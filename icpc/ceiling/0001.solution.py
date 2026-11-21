def same_or_not(a, b):
    if len(a) != len(b):
        return False
    if len(a) <= 1:
        return True

    al, ar = [], []
    bl, br = [], []

    for i in range(1, len(a)):
        if a[i] < a[0]:
            al.append(a[i])
        else:
            ar.append(a[i])

        if b[i] < b[0]:
            bl.append(b[i])
        else:
            br.append(b[i])

    return same_or_not(al, bl) and same_or_not(ar, br)


N, K = map(int, input().strip().split())
trees = []
counts = 0

for _ in range(N):
    nums = list(map(int, input().strip().split()))

    for t in trees:
        if same_or_not(nums, t):
            break
    else:
        # Runs only if no matching tree shape was found
        counts += 1
        trees.append(nums)

print(counts)