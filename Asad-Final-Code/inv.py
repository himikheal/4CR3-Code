import time

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def modular_inverse_euler(a, m):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    
    phi_m = m-1
    # Using modular exponentiation
    return pow(a, phi_m - 1, m)


def extended_euclidean(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t  # gcd, x (inverse), y

def modular_inverse_euclidean(a, m):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    
    gcd_val, x, _ = extended_euclidean(a, m)
    if gcd_val != 1:
        raise ValueError("Inverse does not exist.")
    
    return x % m  # Ensure the result is positive

# Elgamal signature ephemeral key counter

p = 953
counter = 0
for i in range(p-2):
    if (gcd(i, p-1) == 1):
        counter += 1
print(counter)