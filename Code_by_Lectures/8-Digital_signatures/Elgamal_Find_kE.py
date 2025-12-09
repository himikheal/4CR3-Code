# Signature generation:
# Input:  x,d 

# Choose a random ephemeral key  kE∈{0,1,…,p−2}  such that  gcd(kE,p−1)=1 
# Compute  r=αkE(modp)  and  s=(x−d⋅r)k−1E(modp−1) 
# Return  (r,s) 
# Signature verification:
# Input:  x,(r,s) 

# Compute  t=βr⋅rs(modp) 
# Return “invalid” if  t≠αx(modp) ; otherwise return “valid.”

# ElGamal reused-k recovery script

p = 669379343040372993112682310767
alpha = 471320288183839082507675912725
beta = 503223353403473572856131255764

# message/signature 1
x1 = 101642072077707199087278299367
r1 = 39046851009170557969179155854
s1 = 463142876672892811270873974035

# message/signature 2
x2 = 250176895235233435828178990580
r2 = 39046851009170557969179155854
s2 = 334254431083127010187873286118

mod = p - 1  # signatures use exponent modulus p-1

# compute numerator and denominator modulo (p-1)
num = (x1 - x2) % mod
den = (s1 - s2) % mod

# modular inverse of denominator modulo (p-1)
inv_den = pow(den, -1, mod)

# compute k
kE = (num * inv_den) % mod

print("Recovered ephemeral key kE =")
print(kE)

# verify that alpha^kE % p == r
r_check = pow(alpha, kE, p)
print("\nVerification:")
print("r from signatures:   ", r1)
print("alpha^kE mod p (r):  ", r_check)
print("Match with r1 ", r_check == r1)
print("Match with r2 ", r_check == r2)
