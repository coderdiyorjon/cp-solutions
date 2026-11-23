n = int(input())
s = map(str, input().split())
s = tuple((i[0], int(i[1:])) for i in s)

direction_map = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
x, y = 0, 0
coordinates = [(x, y)]

for d, dist in s:
    x += direction_map[d][0] * dist
    y += direction_map[d][1] * dist
    coordinates.append((x, y))

sum1, sum2 = 0, 0
for i in range(len(coordinates) - 1):
    sum1 += coordinates[i][0] * coordinates[i + 1][1]
    sum2 += coordinates[i + 1][0] * coordinates[i][1]

print(f"THE AREA IS {abs(sum1 - sum2) // 2}")
