def mod_inverse(a, m):
    """Compute the modular inverse of a under modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Public parameters
p = 59  # Prime number
q = 29  # Prime divisor
alpha = 3  # Generator

# Private key and public key generation
d = 23  # Private key
beta = pow(alpha, d, p)  # Public key
print(f"Public parameters: p = {p}, q = {q}, alpha = {alpha}")
print(f"Public key (beta) = {beta}")

# Message and hash
x = 41  # Message
h_x = 17  # Hash of message
print(f"Message: x = {x}, h(x) = {h_x}")

# Signature generation
k_e = 25  # Random ephemeral key
r = pow(alpha, k_e, p) % q
k_e_inv = mod_inverse(k_e, q)
s = (h_x + d * r) * k_e_inv % q
print(f"Signature generation:")
print(f"k_e = {k_e}")
print(f"r = {r}")
print(f"s = {s}")

# Signature verification
w = mod_inverse(s, q)
u1 = (w * h_x) % q
u2 = (w * r) % q
v = (pow(alpha, u1, p) * pow(beta, u2, p)) % p % q
print(f"\nSignature verification:")
print(f"w = {w}")
print(f"u1 = {u1}")
print(f"u2 = {u2}")
print(f"v = {v}")

# Verify if signature is valid
print("\nVerification result:")
print("Valid signature" if v == r else "Invalid signature")