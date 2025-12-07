# Modular Arithmetic
# Modulo operation:
# a ≡ r mod m
# Remainder Modulus
# • It means m | a − r (m divides a − r)
# • Equivalently, a = mq + r for some integer q

# We compute modular division by multiplying by the inverse, i.e. a/b mod m is ab^(−1) mod m
# The inverse b^(−1) exists only if gcd(b, m) = 1

# Modular reduction can be performed at any point of computation
# • Example: exponentiation
# ▶ Modular reduction at the end:
# 75 = 16807 ≡ 11 mod 13
# ▶ Modular reduction throughout:
# 7^5 = 7^2 · 7^2 · 7 ≡ 10 · 10 · 7 ≡ 11 mod 13