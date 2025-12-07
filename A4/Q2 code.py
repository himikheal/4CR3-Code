def dlp_base3(g, h, p, n):
    """
    Computes x such that g^x ≡ h (mod p)
    assuming the order of g divides 3^n.

    Returns x and the list of base-3 digits [x0, x1, ..., x_{n-1}].
    """

    x_digits = []  # store digits x0, x1, ...
    current_h = h
    current_g = g

    for i in range(n):
        # exponent is 3^(n-k-1)
        exp = 3 ** (n - i - 1)

        # Compute t = h^(3^(n-k-1))
        t = pow(current_h, exp, p)

        # Compute base = g^(3^(n-k-1))
        base = pow(current_g, exp, p)

        # Find digit d ∈ {0,1,2} by matching t = base^d
        digit = None
        if t == 1:
            digit = 0
        elif t == base:
            digit = 1
        elif t == pow(base, 2, p):
            digit = 2
        else:
            raise ValueError("Digit not found — g may not have order 3^n")

        x_digits.append(digit)

        # Update h ← h * g^(-digit)
        if digit != 0:
            inv = pow(current_g, -digit, p)  # modular inverse via pow
            current_h = (current_h * inv) % p

        # Update g ← g^3
        current_g = pow(current_g, 3, p)

    # reconstruct x from digits
    x = 0
    for i, d in enumerate(x_digits):
        x += d * (3 ** i)

    return x, x_digits

print(dlp_base3(4, 17, 19, 2))  # Should output (5, [2, 1]) since 4^5 = 17 mod 19

p = 20602102921755074907947094535687
g = 15074692835850319635499377698538
n = 65
h = 19341277950553269760848569026015
print(dlp_base3(g, h, p, n))