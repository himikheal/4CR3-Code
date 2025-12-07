# s0 = 1, t0 = 0
# s1 = 0, t1 = 1
# i = 1
# do
# i = i + 1
# ri = ri−2 mod ri−1
# qi−1 = (ri−2 − ri)/ri−1
# si = si−2 − qi−1si−1
# ti = ti−2 − qi−1ti−1
# while ri ̸ = 0
# return gcd(r0, r1) = ri−1, s = si−1, t = ti−1

def extended_euclidean(a, b):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r0, r1 = a, b
    i = 1

    while r1 != 0:
        i += 1
        r2 = r0 % r1
        q = (r0 - r2) // r1
        s2 = s0 - q * s1
        t2 = t0 - q * t1

        r0, r1 = r1, r2
        s0, s1 = s1, s2
        t0, t1 = t1, t2

    return r0, s0, t0  # gcd, s, t

# Use the extended euclidean algorithm to find modular inverse
# we compute r and s such that ra + sb = 1
# then the inverse of a (mod b) is r
# suppose a = 76523743 and b = 32486298361
# find r and s such that ra + sb = 1

a = 76523743
b = 32486298361
gcd, r, s = extended_euclidean(a, b)
if gcd == 1:
    print(f"The modular inverse of {a} modulo {b} is {r % b}")
    print("r and s are:", r, s)

