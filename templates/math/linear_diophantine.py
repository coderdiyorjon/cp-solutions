def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Finds x and y such that a*x + b*y = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    d: int
    x1: int
    y1: int
    d, x1, y1 = extended_gcd(b, a % b)
    return d, y1, x1 - y1 * (a // b)


def find_any_solution(a: int, b: int, c: int) -> tuple[bool, int, int, int]:
    """Finds a single valid solution to a*x + b*y = c.

    Returns:
        tuple: (found(bool), x, y, gcd)
    """
    g: int
    x: int
    y: int
    g, x, y = extended_gcd(abs(a), abs(b))
    if c % g != 0:
        return False, 0, 0, 0

    x *= c // g
    y *= c // g

    if a < 0: x = -x
    if b < 0: y = -y

    return True, x, y, g


def solve_interval(a: int, b: int, c: int, minx: int, maxx: int, miny: int, maxy: int) -> int:
    """Finds the number of solutions to a*x + b*y = c in a bounded interval.
    x must be in [minx, maxx] and y must be in [miny, maxy].
    """
    # Degenerate case: a = 0 and b = 0
    if a == 0 and b == 0:
        if c == 0:
            return (maxx - minx + 1) * (maxy - miny + 1)
        return 0

    # Degenerate cases: one of the coefficients is 0
    if a == 0:
        if c % b == 0 and miny <= c // b <= maxy:
            return maxx - minx + 1
        return 0
    if b == 0:
        if c % a == 0 and minx <= c // a <= maxx:
            return maxy - miny + 1
        return 0

    # 1. Find any base solution
    found: bool
    x: int
    y: int
    g: int
    found, x, y, g = find_any_solution(a, b, c)
    if not found:
        return 0

    # Simplify the equaion by dividing by GCD
    a //= g
    b //= g
    c //= g

    sign_a: int = 1 if a > 0 else -1
    sign_b: int = 1 if b > 0 else -1

    # Shift function to move x and y by steps of 'b' and 'a' respectively
    def shift_solution(x: int, y: int, a: int, b: int, cnt: int) -> tuple[int, int]:
        return x + cnt * b, y - cnt * a

    # Find boundaries for x [lx1, rx1]
    cnt1: int = (minx - x) // b
    x_sh: int
    y_sh: int
    x_sh, y_sh = shift_solution(x, y, a, b, cnt1)
    if x_sh < minx:
        x_sh, y_sh = shift_solution(x_sh, y_sh, a, b, sign_b)
    lx1: int = x_sh

    cnt2: int = (maxx - x) // b
    x_sh, y_sh = shift_solution(x, y, a, b, cnt2)
    if x_sh > maxx:
        x_sh, y_sh = shift_solution(x_sh, y_sh, a, b, -sign_b)
    rx1: int = x_sh

    if lx1 > rx1:
        lx1, rx1 = rx1, lx1

    # Find boundaries for y [lx2, rx2]
    cnt3: int = -((miny - y) // a)
    x_sh, y_sh = shift_solution(x, y, a, b, cnt3)
    if y_sh < miny:
        x_sh, y_sh = shift_solution(x_sh, y_sh, a, b, -sign_a)
    lx2: int = x_sh

    cnt4: int = -((maxy - y) // a)
    x_sh, y_sh = shift_solution(x, y, a, b, cnt4)
    if y_sh > maxy:
        x_sh, y_sh = shift_solution(x_sh, y_sh, a, b, sign_a)
    rx2: int = x_sh

    if lx2 > rx2: 
        lx2, rx2 = rx2, lx2

    # Find the intersection of the two intervals
    lx: int = max(lx1, lx2)
    rx: int = min(rx1, rx2)

    if lx > rx:
        return 0

    return (rx - lx) // abs(b) + 1