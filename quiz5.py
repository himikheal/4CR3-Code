# Consider the following parameters for the elgamal signature schemeL

p = 669379343040372993112682310767
alpha = 471320288183839082507675912725
beta = 503223353403473572856131255764

# Bob accidentally reuses the same ephermeral key when signing two distinct messages x1, x2
# This results in the two signatures:

x1 = 101642072077707199087278299367
r1 = 39046851009170557969179155854
s1 = 463142876672892811270873974035

x2 = 250176895235233435828178990580
r2 = 39046851009170557969179155854
s2 = 334254431083127010187873286118

# Find the ephermeral key kE

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

kE = (modinv(s1 - s2, p - 1) * (x1 - x2)) % (p - 1)
print("The ephemeral key kE is:", kE)

print(pow(alpha, kE, p) == r1)
print(pow(alpha, kE, p) == r2)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(kE, p-1) == 1)

# x = d · r + kE s (mod p − 1)
print(((x1 - kE * s1) / r1) % (p - 1))
print(((x2 - kE * s2) / r2) % (p - 1))

# beta = alpha^d (mod p)


print("The private key d is:", d)
# Verify that the private key corresponds to the public key
print(pow(alpha, d, p) == beta)
# then the inverse of a (mod b) is r