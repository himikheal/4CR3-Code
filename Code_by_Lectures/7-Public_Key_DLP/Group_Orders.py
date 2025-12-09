# Computing order of an element in Z*_p

p = 11

def order_mod_p(a, p):
    # a is in Z*_p
    for k in range(1, p):
        if pow(a, k, p) == 1:
            return k
    return None

elements = list(range(1, p))
orders = {a: order_mod_p(a, p) for a in elements}

print("Orders of elements in Z*_%d:" % p)
for a, o in orders.items():
    print(f"{a}: {o}")
