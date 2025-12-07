import random

def lfsr(degree, seed, coeffs, output_length=20):
    state = seed.copy()
    for i in range(output_length):
        next_bit = 0
        for j in range(degree):
            next_bit = next_bit + state[i + j] * coeffs[j]
        state.append(next_bit % 2)

    return state


output = lfsr(5, [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], 5)
str1 = ""
for b in output:
    str1 = str1 + str(b)
print(str1)

str2 = ""
for i in range(50):
    str2 = str2 + str(random.randint(0, 1))
print(str2)

# p = 16
# for i in range (32):
#     print(i, pow(i, 3, p), pow(i, 5, p))

p = 31
for i in range(32):
    k = pow(i, 7, p)
    # print(i, k)
    if (i > 1 and i < 31):
        # print(i, k, pow(pow(k, -1, p), 7, p))
        print(i, k, pow(k, 13, p))