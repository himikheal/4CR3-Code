# Baby-Step Giant-Step for DLP: alpha^x = beta mod p
# unverified example

import math

p = 47
alpha = 2
beta = 36

n = p - 1
m = int(math.isqrt(n))

# Step 1: giant steps table
giant = {}
alpha_inv_m = pow(pow(alpha, m, p), -1, p)

value = 1
for j in range(m):
    giant[value] = j
    value = (value * alpha_inv_m) % p

# Step 2: baby steps
value = beta
x = None
for i in range(m):
    if value in giant:
        x = i * m + giant[value]
        break
    value = (value * alpha) % p

print("Discrete log x =", x)
