# It was explained in class that for a pair of numbers (a,b) such that gcd(a,b) = 1, 
# we can compute the inverse of a (mod b) using the extended euclidean algorithm: 
# we compute r and s such that ra + sb = 1. Then the inverse of a (mod b) is r. 
# Suppose a = 76523743 and b = 32486298361. Find r and s. 

a = 76523743
b = 32486298361

# eq = r*a + s*b = 1

# gcd(a, b) = 1

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

gcd_value, r, s = extended_gcd(a, b)
print(f"gcd({a}, {b}) = {gcd_value}")
print(f"r = {r}, s = {s}")

# r = 4441036324, s = −10461171

# Verify that ra + sb = 1
verify = r * a + s * b
print(f"Verification: {r} * {a} + {s} * {b} = {verify}")

# using pseudocode from class
def extended_euclidean(r0, r1):
    # Initialize
    s0, t0 = 1, 0
    s1, t1 = 0, 1
    i = 1
    
    # Loop until remainder is 0
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    
    # Return gcd and coefficients
    return r0, s0, t0


# Example usage:
# r0 = 76523743
# r1 = 32486298361
# gcd, s, t = extended_euclidean(r0, r1)
# print("gcd =", gcd)
# print("s =", s)
# print("t =", t)

r0 = 112
r1 = 86
gcd, s, t = extended_euclidean(r0, r1)
print("gcd =", gcd)
print("s =", s)
print("t =", t)
print("Verification:", s * r0 + t * r1)  # should equal gcd




