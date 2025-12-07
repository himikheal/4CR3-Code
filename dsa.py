# The Digital Signature Algorithm (DSA)
# Key Generation:
# 1. Generate a prime 21023 < p < 21024
# 2. Find a prime divisor q of p − 1 such that 2159 < q < 2160
# 3. Find an element α ∈ Z×p of order q
# 4. Choose a random integer 0 < d < q
# 5. Compute β = αd (mod p)
# • Public parameters: (p, q, α)
# • Public key: β
# • Private key: d

# The DSA algorithm
p = 899009829279928687167847647253
q = 5938170550372221380503

def generateAlpha(p, q):
    for alpha in range(2, p):
        if pow(alpha, (p - 1) // q, p) != 1:
            return alpha
    return None

alpha = generateAlpha(p, q)
print("Generator alpha is:", alpha) 

  

# Suppose the public primes for the DSA signature scheme are $p = 899009829279928687167847647253$ and $q = 5938170550372221380503$. Which of the following is a public key $\beta$ for these parameters?

# A) 428025207316609689260868108104
# B) 511817553315794935894966990404
# C) 52741071529976599941769481354
# D) 430222494411980041758424435195

p = 899009829279928687167847647253
q = 5938170550372221380503
candidates = [
    428025207316609689260868108104,
    511817553315794935894966990404,
    52741071529976599941769481354,
    430222494411980041758424435195
]
for beta in candidates:
  print("Testing beta =", beta)
  print(pow(beta, q, p) == 1)

print(899009829279928687167847647253 % p in candidates)