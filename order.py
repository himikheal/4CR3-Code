import random

def order(a, p):
    """Return the order of a modulo p."""
    if a % p == 0:
        return 0

    # search for smallest k such that a^k ≡ 1 (mod p)
    k = 1
    x = a % p
    while x != 1:
        x = (x * a) % p
        k += 1
        if k > p:     # safety (should never happen for prime p)
            return None
    return k

def find_element_of_order_q(p, q):
    """
    Find α ∈ Z_p^× of order exactly q, assuming q | (p−1).
    """
    assert (p - 1) % q == 0, "q must divide p−1"

    # We need an exponent e = (p-1)/q
    e = (p - 1) // q

    while True:
        a = random.randrange(2, p - 1)
        # candidate α = a^e mod p
        alpha = pow(a, e, p)

        # check if alpha has order q
        if pow(alpha, q, p) == 1 and pow(alpha, q // 2, p) != 1:
            return alpha
        
        


print(find_element_of_order_q(2089, 29))