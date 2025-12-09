# Let g : Zp → Zp × Zp, be a PRNG defined by g(x) = (x^3 mod p, x^5 mod p). Is this PRNG secure? Explain.
# (You must investigate whether a sequence of pairs {g(x_i)} can be
# distinguished from a sequence {(a_i, b_i)} where a_i and b_i are uniformly random numbers.)

# This PRNG is not secure since it is periodic to the order of p,
# meaning if p is small enough it will not be secure since it will repeat quickly,
# however if p is too large then the output may never end up looping through the modulus operator
# which would make the output predictable

def g(x, p):
    return (pow(x, 3, p), pow(x, 5, p))

for i in range(25):
    print(g(i, 13))  # Example usage