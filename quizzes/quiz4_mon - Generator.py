# Let p = 22073, a prime number.
# Which one of the following is a generator for the mutiplicative group $(Z_p)^x$ (integers mod p, under multiplication)?
# A) 9386
# B) 4830
# C) 9139
# D) 3655

# Count the order of each candidate
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

# If the order of the candidate is p-1 = 22072, then it is a generator

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