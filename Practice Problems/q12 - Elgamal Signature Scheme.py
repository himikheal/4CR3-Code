# Let p = 953 be a prime number. In the Elgamal signature scheme, Trudy has decided
# to forge a signature by writing a brute-force algorithm that tries all possible ephemeral
# keys. How many trials ephemeral keys does he have to try?
# (a) Less than 219
# (b) Less than 384
# (c) More than 410
# (d) More than 412

# The ephermeral key must be in the range [1, p-2] and coprime to p-1
# Eulers totient is the amount of integers from 1 to n that are coprime to n
# We can use this to find the number of possible ephemeral keys

# prime factors of 952 are 2, 7, and 17
# φ(952) = 952 * (1 - 1/2) * (1 - 1/7) * (1 - 1/17) = 384
# So the answer is (b) Less than 384

import sympy
print("Sympy Eulers Totient of 952:")
print(sympy.totient(952))  # 952 = p-1
print("Prime factors of 952:")
print(sympy.primefactors(952))  # 2^3 * 7 * 17
print("Calculating eulers totient:")
print(952 * (1 - 1/2) * (1 - 1/7) * (1 - 1/17))  # 384

# Or just count how many keys are coprime to p-1 manually

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Elgamal signature ephemeral key counter

p = 953
counter = 0
for i in range(p-2):
    if (gcd(i, p-1) == 1):
        counter += 1
print(counter)