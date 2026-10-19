"""Fibonacci Numbers via Fast Doubling Method.

Calculates the n-th Fibbonacci number in O(log n) time.
Essential for problems where n can be up to 10^18 and the answer
must be output modulo some prime (e.g., 10^9 + 7).
"""

MOD = 10**9 + 7

def fib_fast_doubling(n: int) -> tuple[int, int]:
    """Calculates the pair (F_n, F_{n+1}) modulo MOD in O(log n) time.
    
    Uses the mathematical identities:
    F_{2k}   = F_k + (2 * F_{k+1} - F_k)
    F_{2k+1} = F_k^2 + F_{k+1}^2
    
    Args:
        n (int): The target index in the Fibonacci sequence.
    
    Returns:
        tuple: (F_n % MOD, F_{n+1} % MOD)
    """
    if n == 0:
        return (0, 1)
    
    # Recursively calculate F_k and F_{k+1} where k = n // 2
    a: int
    b: int
    a, b = fib_fast_doubling(n >> 1)
    
    # F_{2k} = F_k * (2 * F_{k+1} - F_k)
    c: int = (a * ((b << 1) - a)) % MOD
    
    # F_{2k+1} = F_k^2 + F_{k+1}^2
    d: int = (a * a + b * b) % MOD
    
    # If n is odd, the pair is (F_{2k+1}, F_{2k+1})
    # Note: F_{2k+2} = F_{2k} + F_{2k+1}
    if n & 1:
        return (d, (c + d) % MOD)
    
    # If n is even, the pair is (F_{2k}, F_{2k+1})
    return (c, d)


def get_fib(n: int) -> function | int:
    """Returns the n-th Fibonacci number modulo MOD."""
    if n < 0:
        return 0
    return fib_fast_doubling(n)[0]


"""Standard O(N) Iterative Approach (for small N < 10^6)"""
def fib_iterative(n: int) -> int:
    """Calculates F_n modulo MOD in O(n) time and O(1) space."""
    if n == 0: return 0
    if n == 1: return 1
    
    a: int
    b: int
    a, b = 0, 0
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    return b
