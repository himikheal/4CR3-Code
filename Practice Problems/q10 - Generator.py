# Which of the following is not a generator for Z^×_953? (All integers are mod 953)
# (a) 602
# (b) 746
# (c) 780
# (d) 94

# 780 is not a generator for the set of all integers mod 953 under multiplication

a_count = 0
while True:
    a_count += 1
    if pow(602, a_count, 953) == 1:
        break

b_count = 0
while True:
    b_count += 1
    if pow(746, b_count, 953) == 1:
        break

c_count = 0
while True:
    c_count += 1
    if pow(780, c_count, 953) == 1:
        break

d_count = 0
while True:
    d_count += 1
    if pow(94, d_count, 953) == 1:
        break

print("Order of 9386:", a_count)
print("Order of 4830:", b_count)
print("Order of 9139:", c_count)
print("Order of 3655:", d_count)

print("Non-Generator is:", end=" ")
if a_count != 952:
    print("602")
elif b_count != 952:
    print("746")
elif c_count != 952:
    print("780")
elif d_count != 952:
    print("94")
else:
    print("None")