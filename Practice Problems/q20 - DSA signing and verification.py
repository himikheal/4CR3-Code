# The parameters of a DSA scheme are given by
# p = 59,
# q = 29,
# α = 3,
# and Bob’s private key is 
# d = 23.
# Show the process of signing (by Bob) and verification (by Alice) 
# for the following hashed messages h(x) and ephemeral keys kE:
# (a) h(x) = 17, kE = 25
# (b) h(x) = 2, kE = 13

# PART (a)
# Signature for (h(x) = 17, kE = 25):
# r = (alpha ^ kE mod p) (mod q)
# r = (3 ^ 25 mod 59) (mod 29)
# r = 22
# s = (h(x) + d · r) * kE_inv (mod q)
# s = (17 + 23 · 22) * 7 (mod 29)
# s = 7

# Verification for (h(x) = 17, kE = 25):
# w = s_inv (mod q)
# w = 25 (mod 29)
# w = 25
# u_1 = w * h(x) (mod q)
# u_1 = 25 * 17 (mod 29)
# u_1 = 19
# u_2 = w * r (mod q)
# u_2 = 25 * 22 (mod 29)
# u_2 = 28
# t = (alpha^u_1 * beta^u_2 mod p) (mod q)
# t = (3^19 * 45^28 mod 59) (mod 29)
# t = 22
# Signature using h(x) = 17, kE = 25 is valid

# PART (b)
# Signature for (h(x) = 2, kE = 13):
# r = (alpha ^ kE mod p) (mod q)
# r = (3 ^ 13 mod 59) (mod 29)
# r = 25
# s = (h(x) + d · r) * kE_inv (mod q)
# s = (2 + 23 · 25) * 9 (mod 29)
# s = 2

# Verification for (h(x) = 2, kE = 13):
# w = s_inv (mod q)
# w = 15 (mod 29)
# w = 15
# u_1 = w * h(x) (mod q)
# u_1 = 15 * 2 (mod 29)
# u_1 = 1
# u_2 = w * r (mod q)
# u_2 = 15 * 25 (mod 29)
# u_2 = 27
# t = (alpha^u_1 * beta^u_2 mod p) (mod q)
# t = (3^1 * 45^27 mod 59) (mod 29)
# t = 25
# Signature using h(x) = 2, kE = 13 is valid



def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % m

p = 59
q = 29
alpha = 3
d = 23
beta = pow(alpha, d, p)

# Signature generation
# r = (α^kE mod p) (mod q)
# s = (h(x) + d · r)kE^{−1} (mod q)
def sign(hx, d, kE):
    r = pow(alpha, kE, p) % q
    kE_inv = mod_inverse(kE, q)
    s = ((hx + d * r) * kE_inv) % q
    return r, s, kE_inv

# Signature verification:
# w = s^{−1} (mod q)
# u_1 = wh(x) (mod q)
# u_2 = wr (mod q)
# t = (α^u_1 β^u_2 mod p) (mod q)
# Valid if t = r
def verify(hx, r, s):
    w = mod_inverse(s, q)
    u_1 = (w * hx) % q
    u_2 = (w * r) % q
    t = (pow(alpha, u_1, p) * pow(beta, u_2, p)) % p % q
    return w, u_1, u_2, t, t == r

def print_process(hx, kE):
    r, s, kE_inv = sign(hx, d, kE)
    w, u_1, u_2, t, is_valid = verify(hx, r, s)
    print(f"Signature for (h(x) = {hx}, kE = {kE}):")
    print(f"r = (alpha ^ kE mod p) (mod q)")
    print(f"r = ({alpha} ^ {kE} mod {p}) (mod {q})")
    print(f"r = {r}")
    print(f"s = (h(x) + d · r) * kE_inv (mod q)")
    print(f"s = ({hx} + {d} · {r}) * {kE_inv} (mod {q})")
    print(f"s = {s}")

    print()
    print(f"Verification for (h(x) = {hx}, kE = {kE}):")
    print(f"w = s_inv (mod q)")
    print(f"w = {mod_inverse(s, q)} (mod {q})")
    print(f"w = {w}")
    print(f"u_1 = w * h(x) (mod q)")
    print(f"u_1 = {w} * {hx} (mod {q})")
    print(f"u_1 = {u_1}")
    print(f"u_2 = w * r (mod q)")
    print(f"u_2 = {w} * {r} (mod {q})")
    print(f"u_2 = {u_2}")
    print(f"t = (alpha^u_1 * beta^u_2 mod p) (mod q)")
    print(f"t = ({alpha}^{u_1} * {beta}^{u_2} mod {p}) (mod {q})")
    print(f"t = {t}")

    print(f"Signature using h(x) = {hx}, kE = {kE} is {'valid' if is_valid else 'invalid'}")


# (a) h(x) = 17, kE = 25
hx_a = 17
kE_a = 25

# (b) h(x) = 2, kE = 13
hx_b = 2
kE_b = 13

print()
print_process(hx_a, kE_a)
print()
print_process(hx_b, kE_b)



# DSA Signature Scheme
# Key Generation:
# 1. Generate a prime 2^1023 < p < 2^1024
# 2. Find a prime divisor q of p − 1 such that 2^159 < q < 2^160
# 3. Find an element α ∈ Z×_p of order q
# 4. Choose a random integer 0 < d < q
# 5. Compute β = α^d (mod p)

# Public parameters: (p, q, α)
# Public key: β
# Private key: d

# Signature generation:
# Input: x, d
# 1. Choose a random ephemeral key kE ∈ {0, 1, · · · , q − 1}
# 2. Compute r = (α^kE mod p) (mod q) and s = (h(x) + d · r)kE^{−1} (mod q)
# 3. Return r, s

# Signature verification:
# Input: x, r, s
# 1. Compute w = s^{−1} (mod q), u_1 = wh(x) (mod q), and u_2 = wr (mod q)
# 2. Compute t = (α^u_1 β^u_2 mod p) (mod q)
# 3. Return “valid” if t = r; otherwise return “invalid”