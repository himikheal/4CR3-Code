# Let (n, e) = (493, 205) be the public key in the RSA signature scheme.
# Which of the following is a valid message-signature pair?
# (a) (32, 16)
# (b) (6, 415)
# (c) (53, 83)
# (d) (112, 45)


# The valid message-signature pair is (b) (6, 415)

n = 493
e = 205
x = [32, 6, 53, 112]
s = [16, 415, 83, 45]
for i in range(4):
    if pow(s[i], e, n) == x[i]:
        print("Valid message-signature pair is: (", x[i], ",", s[i], ")")




# RSA Signature Scheme

# generate d, (n, e)
# publish the public key (n, e)
# sign message: s = x^d (mod n)

# verify signature: y = s^e (mod n)
# check if y == x

# Proof of correctness
# s^e = (x^d)^e = x^(de) = x (mod n)