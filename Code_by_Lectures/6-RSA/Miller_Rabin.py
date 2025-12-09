import random

def square_and_multiply(a, e, n):
    result = 1
    base = a % n

    # left-to-right binary exponentiation
    bits = bin(e)[2:]
    for bit in bits:
        result = (result * result) % n
        if bit == '1':
            result = (result * base) % n

    return result


def miller_rabin_test(n, a, d, r):
    """
    Performs a single Miller-Rabin check using base 'a'.
    n : number being tested
    a : chosen base
    d, r : n-1 = 2^r * d with d odd
    """

    # Compute x = a^d mod n
    x = square_and_multiply(a, d, n)

    if x == 1 or x == n - 1:
        return True  # probably prime for this base

    # Repeat r-1 times: x = x^2 mod n
    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return True

    return False  # composite for this base


def miller_rabin(n, k=10):
    """
    Returns True if n is probably prime, False if composite.
    k = number of rounds (more = lower error probability)
    """

    # Handle small cases
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d with d odd
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k rounds
    for _ in range(k):
        a = random.randint(2, n - 2)  # random base
        if not miller_rabin_test(n, a, d, r):
            return False  # definitely composite

    return True  # probably prime

print(miller_rabin(17))      # True
print(miller_rabin(561))     # False (Carmichael composite)
print(miller_rabin(2**61-1)) # probably prime
