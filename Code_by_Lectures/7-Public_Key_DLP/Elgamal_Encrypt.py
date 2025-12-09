# ElGamal Encryption Example
# Public parameters
# unverified example


p = 53
alpha = 27

# Bob's key
b = 12
kB = pow(alpha, b, p)

# Alice's key
a = 32
kA = pow(alpha, a, p)

# Shared key
kAB1 = pow(kB, a, p)
kAB2 = pow(kA, b, p)

# Encrypt plaintext
x = 21
y = (x * kAB1) % p

# Decrypt ciphertext
kAB_inv = pow(kAB1, -1, p)
x_recovered = (y * kAB_inv) % p

print("kA =", kA)
print("kB =", kB)
print("Shared key =", kAB1)
print("Ciphertext =", y)
print("Recovered plaintext =", x_recovered)
