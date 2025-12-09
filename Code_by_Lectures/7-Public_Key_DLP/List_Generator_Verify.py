from sympy import factorint

# p = 22073
# candidates = [9386, 4830, 9139, 3655]

# p = 899009829279928687167847647253
# g = 425044249325748129860331117047
# candidates = [g]

p = 953
candidates = [602, 746, 780, 94]

# Factorize p-1
factors = factorint(p-1)
prime_factors = list(factors.keys())

print(f"Prime factors of {p-1}: {prime_factors}")

def is_generator(g, p, prime_factors):
    for q in prime_factors:
        if pow(g, (p-1)//q, p) == 1:
            print(f"Failed for factor {q}") 
            return False
    return True

for g in candidates:
    if is_generator(g, p, prime_factors):
        print(f"{g} is a generator of (Z_{p})^x")
    else:
        print(f"{g} is NOT a generator")

