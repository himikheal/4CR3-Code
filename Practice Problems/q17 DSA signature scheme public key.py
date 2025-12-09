# Suppose the public primes for the DSA signature scheme are p = 2089 and q = 29. Which
# of the following is a public key β for these parameters?
# (a) 774
# (b) 1762
# (c) 1189
# (d) 512

# (d) 512 is a valid public key β for these parameters.

# Values
p = 2089
q = 29
alpha = 0
generators = []
# Find all generators of order q
for a in range(1, q):
    cycled = False
    d = 0
    # interate d until a^d mod p == 1
    # this finds the order of a
    while not cycled:
        d += 1
        if pow(a, d, p) == 1:
            cycled = True
    # checks if order of a is q
    # if it is, append a to list of generators of order q
    if d == q:
        print(f"{a} is a generator of order {q}")
        alpha = a
        generators.append(a)

print("Generators:", generators)
# check all generators
for generator in generators:
    for beta in [774, 1762, 1189, 512]:
        # check all possible private keys d for given generator and beta
        for d in range(1, q):
            # d is valid if β = α^d (mod p)
            # if valid public key found, print it
            if pow(generator, d, p) == beta:
                print(f"Public key β = {beta} is valid with private key d = {d} and generator α = {generator}")


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