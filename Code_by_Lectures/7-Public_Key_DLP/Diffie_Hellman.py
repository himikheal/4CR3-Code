# Diffie–Hellman Key Exchange
# Given: prime p, generator alpha, private keys a and b
# unverified example

p = 31
alpha = 19

# Alice's private exponent
a = 8
kA = pow(alpha, a, p)

# Bob's private exponent
b = 12
kB = pow(alpha, b, p)

# Shared key (computed two ways)
kAB_from_A = pow(kB, a, p)
kAB_from_B = pow(kA, b, p)

print("kA =", kA)
print("kB =", kB)
print("Shared key from Alice's view:", kAB_from_A)
print("Shared key from Bob's view:", kAB_from_B)
