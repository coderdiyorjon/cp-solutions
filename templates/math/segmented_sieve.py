"""Segmented Sieve of Eratosthenes.

Used to find all prime numbers in the range [L, R].
Crucial when R is ery large (e.g., 10^12) but the range size (R - L)
is managable (e.g., 10^7), preventing Memory Limit Exceeded (MLE).
"""

def segmented_sieve(L: int, R: int) -> list[int]:
    """Finds all prime numbers in the inclusive range [L, R].
    
    Time Complexity: O((R - L + 1) * log(log(R)) + sqrt(R) * log(log(sqrt(R))))
    Space Complexity: O(sqrt(R) + R - L)
    
    Args:
        L (int): Lower bound of the range.
        R (int): Upper bound of the range.
    
    Returns:
        list[int]: List of prime numbers between L and R.
    """
    # Step 1 : Generate all base primes up to sqrt(R) using a standard sieve
    limit: int = int(R**0.5)
    is_prime_base: list[bool] = [True] * (limit + 1)
    base_primes: list[int] = []
    
    for p in range(2, limit + 1):
        if is_prime_base[p]:
            base_primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime_base[i] = False
    
    # Step 2: Initialize a boolean array for the specific range [L, R]
    # is_prime[i] corresponds to the number (i + L)
    range_size: int = R - L + 1
    is_prime: list[bool] = [True] * range_size
    
    # Handle edge cases for 1 and 0
    if L == 0:
        if range_size > 0: is_prime[0] = False
        if range_size > 1: is_prime[1] = False
    elif L == 1:
        if range_size > 0: is_prime[0] = False
    
    # Step 3: Sieve the range [L, R] using the base primes
    for p in base_primes:
        # Find the smallest multiple of p that is >= L
        # We start crossing out at p*p or the first multiple in range, whichever is larger
        start_idx: int = max(p * p, (L + p - 1) // p * p)
        
        # Cross out multiples in the range array
        for j in range(start_idx, R + 1, p):
            is_prime[j - L] = False
        
    # Step 4: Collect all numbers still marked as True
    result: list[int] = []
    for i in range(range_size):
        if is_prime[i]:
            result.append(i + L)
    
    return result
