# It was explained in class that for a pair of numbers (a,b) such that gcd(a,b) = 1,
# we can compute the inverse of a (mod b) using the extended euclidean algorithm:
# we compute r and s such that ra + sb = 1.
# Then the inverse of a (mod b) is r.
# Suppose a = 76523743 and b = 32486298361.
# Find r and s.

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % m

a = 76523743
b = 32486298361
r = mod_inverse(a, b)
s = (1 - r * a) // b
print(f"r: {r}, s: {s}")
# Check that ra + sb = 1
print(f"Check: {r * a + s * b} == 1")