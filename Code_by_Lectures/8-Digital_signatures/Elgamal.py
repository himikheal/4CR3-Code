import random

def elgamal_keygen(p, alpha, a):
    beta = pow(alpha, a, p)
    return (p, alpha, beta), a     # (public key), private key

def egcd(a, b):
    if b == 0: return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError("no inverse")
    return x % m

def elgamal_sign(m, a, p, alpha):
    # pick random k s.t. gcd(k, p-1) = 1
    k = random.randint(2, p-2)
    while egcd(k, p-1)[0] != 1:
        k = random.randint(2, p-2)

    gamma = pow(alpha, k, p)
    k_inv = modinv(k, p-1)

    delta = (k_inv * (m - a * gamma)) % (p - 1)

    return gamma, delta

def elgamal_verify(m, gamma, delta, p, alpha, beta):
    left = (pow(beta, gamma, p) * pow(gamma, delta, p)) % p
    right = pow(alpha, m, p)
    return left == right

# Parameters (example small prime set)
p = 467
alpha = 2
a = 127   # private key

# Public key
beta = pow(alpha, a, p)

# Message
m = 123

# Sign
gamma, delta = elgamal_sign(m, a, p, alpha)
print("Signature = (gamma, delta) =", gamma, delta)

# Verify
print("Valid?", elgamal_verify(m, gamma, delta, p, alpha, beta))
