# Suppose n = pq = 437024078297897179,
# phi(n) = 437024076975443440,
# p-q = 28063878.
# Compute p and q


# RSA
# 1. Choose two large primes p, q
# 2. Compute n = pq and φ(n) = (p − 1)(q − 1)
# 3. Select the public exponent e ∈ {0, 1, . . . , φ(n) − 1} such that
#    gcd(e, φ(n)) = 1
# 4. Compute the private key d such that
#    de ≡ 1 mod φ(n)
# 5. Output the private-key, public-key pair (d, e)
#    Technically, the public key is (n, e)

# φ(m) : the number of integers smaller than m that are relatively prime to m

# Euler's Theorem:
# Let a, m > 0 be integers such that gcd(a, m) = 1. Then
# a^(φ(m)) ≡ 1 mod m

n = 437024078297897179
phi_n = 437024076975443440
p_minus_q = 28063878
# We have two equations:
# 1. n = pq
# 2. φ(n) = (p - 1)(q - 1) = pq - p - q + 1 = n - (p + q) + 1
# From equation 2, we can express p + q:
p_plus_q = n - phi_n + 1

# Now we have a system of equations:
# p + q = p_plus_q
# p - q = p_minus_q
# We can solve for p and q:
p = (p_plus_q + p_minus_q) // 2
q = (p_plus_q - p_minus_q) // 2
print("p =", p)
print("q =", q)


