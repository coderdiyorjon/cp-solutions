# Intuition

The floor plan is given as a closed loop of relative cardinal movements (`N`, `S`, `E`, `W`). By anchoring the starting corner at the origin $(0, 0)$ and walking each step, we translate those relative moves into an ordered list of 2D polygon vertices. Once we have the vertices in perimeter order, the **Shoelace Formula** directly yields the exact enclosed area—even if the floor is highly concave or irregularly shaped. [ProblemSource](https://icpc.kattis.com/problems/hardflor)

# Approach

1. **Parse Moves:** Read $n$ and split the instruction tokens into `(direction, distance)` tuples by separating the first character (`i[0]`) from the integer length (`int(i[1:])`).
2. **Trace Coordinates:** Map each cardinal direction to its unit vector (`N`: $(0, 1)$, `S`: $(0, -1)$, `E`: $(1, 0)$, `W`: $(-1, 0)$). Starting at `(0, 0)`, update `(x, y)` for each move and append it to `coordinates`. Because the floor boundary is a closed loop, the final appended vertex naturally returns to `(0, 0)`.
3. **Apply the Shoelace Formula:** Loop through every adjacent pair of vertices $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, accumulating:

$$\text{sum}_1 = \sum_{i=0}^{n-1} x_i y_{i+1}, \qquad \text{sum}_2 = \sum_{i=0}^{n-1} x_{i+1} y_i$$


4. **Exact Integer Area:** Since every edge is axis-aligned with integer lengths, the area is guaranteed to be an integer. Taking `abs(sum1 - sum2) // 2` avoids floating-point division entirely and prints the result in the exact `THE AREA IS <area>` format required by Kattis.

# Complexity

* Time complexity:
$\mathcal{O}(N)$
Parsing the $N$ tokens, building the $N + 1$ vertices, and evaluating the Shoelace sums each require a single linear pass over the input.
* Space complexity:
$\mathcal{O}(N)$
Stores the parsed tuple `s` of length $N$ and the `coordinates` list of length $N + 1$.

# Code

```python
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

```
