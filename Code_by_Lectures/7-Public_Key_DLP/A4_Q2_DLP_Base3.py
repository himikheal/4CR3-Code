def solve_dlp():
    p = 20602102921755074907947094535687
    g = 15074692835850319635499377698538
    h = 19341277950553269760848569026015
    n = 65

    # 1. Inverse of g modulo p
    g_inv = pow(g, -1, p)

    # 2. Precompute gamma = g^(3^(n-1))
    gamma = pow(g, 3**(n-1), p)

    # 3. Create Lookup Table
    lookup = {pow(gamma, i, p): i for i in range(3)}

    x = 0
    current_h = h

    # 4. Main Loop
    for k in range(n):
        # Isolate the digit: raise current_h to 3^(n-1-k)
        isolation_exp = 3**(n - 1 - k)
        target = pow(current_h, isolation_exp, p)
        
        # Find digit
        d = lookup[target]
        
        # Accumulate result
        x += d * (3**k)
        
        # Update h: remove the found factor
        # Multiply by g^(-d * 3^k)
        correction_exp = d * (3**k)
        correction = pow(g_inv, correction_exp, p)
        current_h = (current_h * correction) % p

    return x

print(solve_dlp())

# output = 2621519338154903134624454481960