# Let G be a finite cyclic group of size N, and let g ∈ G be a generator. 
# Suppose Trudy has access to an oracle that can solve the computational Diffie-Hellman problem,
# i.e., for any 1 ≤ x, y < N , given g^x and g^y, Trudy can efficiently compute g^(xy) by calling the oracle.
# Can Trudy solve the following problem efficiently:
# given g^x and n ∈ O(log(N)), compute g^(x^n+3x^2+x+5).


# g^(x^n+3x^2+x+5) = g^(x^n) * g^(3x^2) * g^(x) * g^(5)
# Trudy can compute g^(x^n) using the oracle by repeated squaring through binary exponentiation
# Trudy can compute g^(3x^2) using the oracle where y = 3x
# Trudy can compute g^(x) directly since it is given
# g^(5) can be computed directly since it is a constant

# With all these terms it would take 3 more multiplications to get the final result
# Thus, Trudy can compute g^(x^n+3x^2+x+5) efficiently using the oracle