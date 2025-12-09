# Let p be a large prime such that 7 does not divide p − 1.
# Define the function f : Zp → Zp by f (x) = x^7 mod p.
# Is f a one-way function? Explain.

# A one-way function is a function that is easy to compute in one direction,
# but hard to invert (i.e., given y = f(x), it is computationally infeasible to find x).
# To determine if f(x) = x^7 mod p is a one-way function,
# we need to analyze whether it is easy to compute f(x) and whether it is hard to invert f(x).

# If 7 does not divide p - 1, then 7 and p - 1 are coprime.
# gcd(7, p - 1) = 1
# Using the extended Euclidean algorithm, we can find integers a and b such that
# 7a + (p-1)b = 1
# Taking this to (mod p-1), we get
# 7a ≡ 1 (mod p-1)
# Since

# x^a ≡ x^b (mod p) 
# whenever
# a ≡ b (mod p-1)

# This means that
# x^(7a) ≡ x (mod p)

# Proof below

# Given 7a ≡ 1 (mod p-1), we know that for any number k,
# 7a = 1 + k(p-1)
# Therefore,
# x^(7a) = x^(1 + k(p-1)) (mod p)
# = x * (x^(k(p-1))) (mod p)
# = x * (x^(p-1))^k (mod p)
# ≡ x * 1^k (mod p)  (by Fermat's Little Theorem)
# ≡ x (mod p)

# x^(7a) ≡ x (mod p)
# (x^7)^a ≡ x (mod p)
# x^7 = f(x) = y
# Therefore,
# f(x)^a ≡ x (mod p)
# This shows that we can compute the inverse of f(x) efficiently using modular exponentiation.
# Hence, f(x) is not a one-way function.








# The modular inverse of a number a modulo m is a number x such that ax = 1 (mod m).
# This is equivalent to saying that m divides ax - 1,
# meaning ax - 1 = km for some integer k,
# or ax = 1 + km.
# The modular inverse only exists if a and m are coprime.

# Fermat's little theorem
# if p is a prime number, then for any integer a,
# a^p - a is a multiple of p.
# Equivalently, a^p ≡ a (mod p).
# If a is not divisible by p, then
# a^(p-1) ≡ 1 (mod p)

# Example:
# 2^(17-1) = 1 mod (17)
# 65536 mod 17 = 1
# Therefore, (65536-1) is a multiple of 17
