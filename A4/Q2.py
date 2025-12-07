# DLP_base3(g, h, n):
#     x = 0
#     current = h

#     for k from n-1 down to 0:
#         t = current^(3^k)     # compute g^(x mod 3)

#         # Try digit = 0, 1, 2
#         for d in {0,1,2}:
#             if t == g^(d * 3^k):
#                 x_k = d
#                 break

#         # Remove this digit from current
#         current = current * (g^(-d * 3^k))

#         # Add digit to answer
#         x = x + d * 3^k

#     return x

def DLP_base3(a, b, n, p):
    x = 0
    current = b
    for k in range(n-1, -1, -1):
        t = pow(current, pow(3, k), p)

        # Try digit = 0, 1, 2
        for d in range(3):
            if t == pow(a, d * pow(3, k), p):
                x_k = d
                break

        # Remove this digit from current
        current = (current * pow(a, -d * pow(3, k), p)) % p

        # Add digit to answer
        x += d * pow(3, k)

    return x

n = 2
a = 4
b = 17
p = 19
print("x =", DLP_base3(a, b, n, p))

print(pow(4,8))
print(pow(4, 8, 19))

group = []
for i in range(10):
    group.append(pow(4, i, 19))
print("Group =", group)