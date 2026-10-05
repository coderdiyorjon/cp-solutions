"""Binary Exponentation (Fast Power) and Modular Inverse.

Note: For standard integer modular exponentation in Python,
always use the built-in `pow(base, exp, mod)` as it is faster.
These templates are useful for custom objects (like Matrices)
or understanding the underlyingg algorithm.
"""

def binpow(a: int, b: int) -> int:
    """Calculates a^b in O(log b) time."""
    res = 1
    while b > 0:
        # If the current power is odd, multiply the result by 'a'
        if b & 1:
            res = res * a
        # Square the base and halve the power
        a = a * a
        b >>= 1
    return res


def binpow_mod(a: int, b: int, m: int) -> int:
    """Calculates a^b mod m in O(log b) time."""
    a %= m
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res


def mod_inverse_format(a: int, m: int) -> int:
    """Calculates the modular multiplicative inverse of 'a' modulo 'm'.
    
    WARNING: This ONLY works if 'm' is a prime number (e.g., 10^9 + 7).
    It uses Fermat's Little Theorem: a^(m - 1) ≡ 1 (mod m) -> a ^ (-1) ≡ a ^ (m - 2) (mod m).
    
    Time Complexity: O(log m)
    """
    # In practise, just use: return pow(a, m-2, m)
    return binpow_mod(a, m - 2, m)
