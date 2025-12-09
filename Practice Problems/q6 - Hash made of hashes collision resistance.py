# Let h1 and h2 be two collision resistant hash functions. Define g(x) = h1(h2(x)).
# Is g collision resistant? Explain.

# Collision resistance means that it is computationally infeasible to find two distinct inputs x and y such that h(x) = h(y).
# Assume g is not collision resistant. This means there exist distinct inputs x and y such that g(x) = g(y).
# Therefore, there exist inputs such that h1(h2(x)) = h1(h2(y)).
# Since h2 is a collision resistant hash function, it must output distinct hashes for the distinct inputs x and y.
# Call these inputs a = h2(x) and b = h2(y).
# a != b
# However, h1(a) = h1(b), meaning h1 is not collision resistant.
# This cannot be true, therefore proving g is collision resistant by contradiction.