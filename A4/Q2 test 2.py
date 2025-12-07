def dlp(g, h, p, n):
    x_digits = []

    for i in range(n):
        # print(x_digits)
        term = pow(h, pow(3, n-i-1), p)

        for y in range(3):
            if pow(pow(g, pow(3, n-i-1), p), y, p) == term:
                x_digits.append(y)
                break
        # print("Found digit:", y)
        
        h = h * pow(g, -x_digits[i], p) % p
        g = pow(g, 3, p)

    x = 0
    for i, d in enumerate(x_digits):
        x += d * (3 ** i)
    return x, x_digits

# print(dlp(4, 17, 19, 2))  # Should output (5, [2, 1]) since 4^5 = 17 mod 19

p = 20602102921755074907947094535687
g = 15074692835850319635499377698538
n = 65
h = 19341277950553269760848569026015
print(dlp(g, h, p, n))

x = 2621519338154903134624454481960
print(pow(g, x, p) == h)  # Should output True