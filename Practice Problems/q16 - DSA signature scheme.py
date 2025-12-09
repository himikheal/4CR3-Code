# In the DSA signature scheme, the public values are (p, q, α),
# where α is a generator of a subgroup of Z×_p of order q.
# Is it safe to fix these public values once and for all,
# so that everyone in the world uses them? Explain.


# It is generally considered safe to fix the public values (p, q, α)
# The security of the DSA signature scheme relies on the difficulty of the discrete logarithm problem
# That is, given α and β = α^x (mod p), it is difficult to determine x.

# Theroetically, if (p, q, α) are fixed and widely known,
# the chosen d value is not affected, as long as d is kept secret and chosen randomly for each user.
# Fixing the public parameters narrows the potiential values of d,
# but as long as the dlp problem remains hard in this group, due to the size of p and q,
# the security of individual private keys is not compromised.






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