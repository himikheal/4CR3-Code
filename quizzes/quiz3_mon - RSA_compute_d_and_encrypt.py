# In the plain RSA ecnryption scheme, suppose p = 447106507, q = 5940619.
# Suppose the public exponent is e = 53. What are the private key d and the encryption of the message 983472?

# RSA Encryption Scheme
# Key Generation
# 1. Choose two large primes p, q
# 2. Compute n = pq and φ(n) = (p − 1)(q − 1)
# 3. Select the public exponent e ∈ {0, 1, . . . , φ(n) − 1} such that
# gcd(e, φ(n)) = 1
# 4. Compute the private key d such that
# de ≡ 1 mod φ(n)
# 5. Output the private-key, public-key pair (d, e)
# Technically, the public key is (n, e).

# Encryption, Decryption
# Input: public key (n, e) and plaintext x.
# 1. Compute y = x^e mod n
# 2. Return y
# Input: Input: private key d and ciphertext y.
# 1. Compute x = yd mod n
# 2. Return x

p = 447106507
q = 5940619
e = 53

n = p * q
phi_n = (p - 1) * (q - 1)

# Compute d
# formula for modular inverse of e mod phi(n)
# d ≡ e^(-1) mod φ(n)
d = pow(e, -1, phi_n)

# Encrypt the message
message = 983472
ciphertext = pow(message, e, n)
print("Private key d =", d)
print("Ciphertext =", ciphertext)