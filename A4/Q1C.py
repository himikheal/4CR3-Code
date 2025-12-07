import primefac

p = 899009829279928687167847647253
g = 425044249325748129860331117047

def is_generator(g, p):
    for factor in primefac.primefac(p - 1):
        print("Testing factor:", factor)
        if pow(g, (p - 1) // factor, p) == 1:
            print("Failed for factor:", factor)
            print("p-1 // factor =", (p - 1) // factor)
            print("g^(p-1/factor) mod p =", pow(g, (p - 1) // factor, p))
            return False
    return True

print("Is g a generator of Z_p*?", is_generator(g, p))