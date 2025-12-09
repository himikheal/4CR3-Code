# eg in slides
# p = 53
# q = 13
# a = 10      # generator g
# d = 8     # private key x
# h = 6     # hash(message)
# kE = 9    # nonce k

# # 20a
# p = 50
# q = 29
# a = 3      # generator g
# d = 23     # private key x
# h = 17     # hash(message)
# kE = 25    # nonce k

# 20b
p = 59
q = 29
a = 3      # generator g
d = 23     # private key x
h = 2     # hash(message)
kE = 13    # nonce k

# Public key
b = pow(a, d, p)
print("b =", b)

# ------------------------
# SIGNATURE GENERATION
# ------------------------

# r = (a^k mod p) mod q
r = pow(a, kE, p) % q
print("r =", r)

# s = k^{-1} * (h + d*r) mod q
# Compute k^{-1} mod q
k_inv = pow(kE, -1, q)

s = (k_inv * (h + d * r)) % q
print("s =", s)

# ------------------------
# VERIFICATION
# ------------------------

# w = s^{-1} mod q
w = pow(s, -1, q)
print("w =", w)

# u1 = h * w mod q
u1 = (h * w) % q
print("u1 =", u1)

# u2 = r * w mod q
u2 = (r * w) % q
print("u2 =", u2)

# v = ((a^u1 * b^u2) mod p) mod q
v = (pow(a, u1, p) * pow(b, u2, p) % p) % q
print("v =", v)

print("Signature valid:", v == r)
