# Pollard's Rho for DLP α^x = β mod p
# Simplified version suitable for exam-level illustration
# unverified example

p = 43
alpha = 2
beta = 36
n = p - 1  # order of Z*_p

# partition function
def f(x, a, b):
    if x % 3 == 0:
        return (x * beta % p, a, (b + 1) % n)
    elif x % 3 == 1:
        return (x * x % p, (a * 2) % n, (b * 2) % n)
    else:
        return (x * alpha % p, (a + 1) % n, b)

# initial
x, a, b = 1, 0, 0
X, A, B = x, a, b

while True:
    x, a, b = f(x, a, b)
    X, A, B = f(*f(X, A, B))
    if x == X:
        break

# Solve (a - A) + x (B - b) ≡ 0 mod n
num = (a - A) % n
den = (B - b) % n
inv = pow(den, -1, n)
x_solution = (num * inv) % n

print("Pollard Rho discrete log = ", x_solution)
