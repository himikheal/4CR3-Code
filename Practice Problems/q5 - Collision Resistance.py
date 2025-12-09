# Let u ∈ Z^n_p be a fixed vector of length n with entries in Z_p.
# Define a hash function
# f_u : Z^n_p → Z_p by f_u(v) = ⟨u, v⟩ = u_1 * v_1 + · · · + u_n * v_n mod p.
# Is this hash function collision-resistant? Explain.

# No, this hash function is not collision-resistant.
# A collision occurs when two different inputs produce the same hash output.
# Since f_u is a linear function, we can find collisions easily.
# There are infinitely many vectors v that can produce the same dot product with u modulo p.
# Meaning it is computationally feasible to find two distinct inputs v1 and v2 such that f_u(v1) = f_u(v2).
# Therefore, the hash function f_u is not collision-resistant.


p = 7
u = [1, 2]
v1 = [3, 4]
v2 = [9, 1]

def hash_function(u, v, p):
    total = 0
    for ui, vi in zip(u, v):
        print(ui, vi)
        total += ui * vi

    return total % p

print("Hash of v1:", hash_function(u, v1, 7))
print("Hash of v2:", hash_function(u, v2, 7))

# Cryptographic requirements
# 1. Preimage resistance (or one-wayness)
# 2. Second preimage resistance (or weak collision resistance)
# 3. Collision resistance (or strong collision resistance)

# Preimage resistance:
# Given a hash value h, it should be computationally infeasible to find any input x such that f(x) = h.

# Seconnd preimage resistance:
# Given an input x1, it should be computationally infeasible to find another input x2 ≠ x1 such that f(x1) = f(x2).

# Collision resistance:
# It should be computationally infeasible to find any two distinct inputs x1 and x2 such that f(x1) = f(x2).