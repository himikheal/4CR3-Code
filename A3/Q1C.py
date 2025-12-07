from math import gcd
import time
import timeit
from sympy import factorint

import numpy as np

a = 1095369562025702556403033673059514719985657846060999038001272754193712036128714475110343472959833158083894277499580078770116751707887313066350958894258
m = 1486849462548131038391075744532018339748969593030811665429204557155898771386352512821463245755183336883785007564272951579651325540287779851348210497897

def extended_gcd(a, b):
    # eucldian alg
    s = {}
    t = {}
    s[0] = 1
    t[0] = 0

    s[1] = 0
    t[1] = 1
    i = 1

    r_0 = b
    r_1 = a
    r = {}
    r[0] = r_0
    r[1] = r_1
    q = {}

    while r[i] != 0:
        i += 1
        r[i] = r[i-2] % r[i-1]

        q[i-1] = (r[i-2] - r[i]) // r[i-1]
        

        s[i] = s[i-2] - q[i-1] * s[i-1]
        t[i] = t[i-2] - q[i-1] * t[i-1]
        
    gcd = r[i-1]
    s_final = s[i-1]
    t_final = t[i-1]

    return (gcd, s_final, t_final)

start = timeit.default_timer()

gcd_value, x, y = extended_gcd(a, m)

end = timeit.default_timer()


print("start", start)
print("e", end)
print(gcd_value)
print(x)
print(y)

print("Time taken for extended euclidean algorithm:", end - start)

def totient(n):
    totient = n
    for factor in factorint(n):
        totient -= totient // factor
    return totient

print("Starting euler's algorithm...")
start = timeit.default_timer()
print(pow(a, totient(m)-1, m))
end = timeit.default_timer()

print("Time taken for euler's algorithm:", end - start)


# 1486849462548131038391075744532018339748969593030811665429204557155898771386352512821463245755183336883785007564272951579651325540287779851348210497895
# 1486849462548131038391075744532018339748969593030811665429204557155898771386352512821463245755183336883785007564272951579651325540287779851348210497895

print(a * y % m)  # should be 1