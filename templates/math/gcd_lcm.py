"""Greatest Common Divisor (GCD) and Extended Euclidean Algorithm.

Note: For standard GCD and LCM, always use Python's built-in
`math.gcd(a, b)` and `math.lcm(a, b)` (Python 3.9+) for optimal speed.
This template is specifically for the Extended Eucledian Algorithm.
"""

import math

def gcd(a: int, b: int) -> int:
    """Standard GCD (fallback if not using math.gcd).
    Time Complexity: O(log(min(a, b)))
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Standard LCM.
    Time Complexity: O(log(min(a, b)))
    """
    return (a // gcd(a, b)) * b if a and b else 0


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Extended Eucledian Algorithm.
    Finds x and y such that: a * x + b * y = gcd(a, b)
    
    Returns:
        tuple: (gcd, x, y)
    Time Complexity: O(log(min(a, b)))
    """
    if b == 0:
        return a, 1, 0
    
    # Recursive call
    d, x1, y1 = extended_gcd(b, a % b)
    
    # Update x and y using results of recursive call
    x = y1
    y = x1 - y1 * (a // b)
    
    return d, x, y


def solve_linear_dophantine(a: int, b: int, c: int) -> tuple[int, int] | None:
    """Solves the equation a * x + b * y = c.
    
    Returns:
        tuple: (x, y) if a solution exists, else None.
    """
    g, x, y = extended_gcd(abs(a), abs(b))
    
    if c % g != 0:
        return None # No solution exists
    
    x *= c // g
    y *= c // g
    
    if a < 0: x = -x
    if b < 0: y = -y
    
    return x, y
