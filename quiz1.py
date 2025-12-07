# HELLO
# RCLLA
# e(k) = (ax + b) mod m
H = ord('H') - ord('A')  # 7
E = ord('E') - ord('A')  # 4
L = ord('L') - ord('A')  # 11
O = ord('O') - ord('A')  # 14

R = ord('R') - ord('A')  # 17
C = ord('C') - ord('A')  # 2
L = ord('L') - ord('A')  # 11
A = ord('A') - ord('A')  # 0

# am + b

print(ord('A') - ord('A'))  # 0

# 17 = a*7 + b mod 26
# 2 = a*4 + b mod 26
# 11 = a*11 + b mod 26
# 0 = a*14 + b mod 26
print("-------")

for i in range(27):
    for j in range(27):
        if (i * 7 + j) % 26 == 17 and (i * 4 + j) % 26 == 2 and (i * 11 + j) % 26 == 11 and (i * 14 + j) % 26 == 0:
            print(i, j)

# a = 5, b = 8
print((H*5 + 8) % 26)
print((E*5 + 8) % 26)
print((L*5 + 8) % 26)
print((O*5 + 8) % 26)

