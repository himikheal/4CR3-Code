from sympy.ntheory import factorint
m = 953-1

factors = factorint(m)
print(f"Prime factorization of {m} with multiplicities:", factors)
prime_factors = list(factors.keys())
print(f"Prime factors of {m}: {prime_factors}")

print((8 - 4) *(7 - 1) *(17-1))