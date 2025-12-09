from math import gcd

# fast trial-division to get distinct prime factors of n
def prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        print(d)
        while n % d == 0:
            # factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors

def is_generator(g, p):
    phi = p - 1
    factors = prime_factors(phi)
    for q in factors:
        print(f"Testing factor {q}")
        if pow(g, phi // q, p) == 1:
            return False
    return True

# given values
p = 899009829279928687167847647253
g = 425044249325748129860331117047

result = is_generator(g, p)
print(result)
