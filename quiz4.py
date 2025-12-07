#Let p = 22073, a prime number. Which one of the following is a generator for the mutiplicative group (Z_p)^x (integers mod p, under multiplication)?

#A) 9386
#B) 4830
#C) 9139
#D) 3655

a_count = 0
while True:
    a_count += 1
    if pow(9386, a_count, 22073) == 1:
        break

b_count = 0
while True:
    b_count += 1
    if pow(4830, b_count, 22073) == 1:
        break

c_count = 0
while True:
    c_count += 1
    if pow(9139, c_count, 22073) == 1:
        break

d_count = 0
while True:
    d_count += 1
    if pow(3655, d_count, 22073) == 1:
        break

print("Order of 9386:", a_count)
print("Order of 4830:", b_count)
print("Order of 9139:", c_count)
print("Order of 3655:", d_count)

print("Generator is:", end=" ")
if a_count == 22072:
    print("9386")
elif b_count == 22072:
    print("4830")
elif c_count == 22072:
    print("9139")
elif d_count == 22072:
    print("3655")
else:
    print("None")

# Euclidean Algorithm to find gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Use the extended euclidean algorithm to find modular inverse
# we compute r and s such that ra + sb = 1
# then the inverse of a (mod b) is r
# suppose a = 76523743 and b = 32486298361
# find r and s such that ra + sb = 1
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % m

a = 76523743
b = 32486298361
r = mod_inverse(a, b)
s = (1 - r * a) // b
print(f"r: {r}, s: {s}")
# Check that ra + sb = 1
print(f"Check: {r * a + s * b} == 1")

# # eucldian alg
# s = {}
# t = {}
# s[0] = 1
# t[0] = 0

# s[1] = 0
# t[1] = 1
# i = 1

# r_0 = m
# r_1 = a
# r = {}
# r[0] = r_0
# r[1] = r_1
# q = {}

# while r[i] != 0:
#     i += 1
#     r[i] = r[i-2] % r[i-1]

#     q[i-1] = (r[i-2] - r[i]) // r[i-1]
    

#     s[i] = s[i-2] - q[i-1] * s[i-1]
#     t[i] = t[i-2] - q[i-1] * t[i-1]

# print(i)

    
# gcd = r[i-1]
# s_final = s[i-1]
# t_final = t[i-1]

# # print("gcd:", gcd)
# # print("t:", t_final)