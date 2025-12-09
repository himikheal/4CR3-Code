# In the plain RSA ecnryption scheme, suppose p = 447106507, q = 5940619. 
# Suppose the public exponent is e = 53. What are the private key d and 
# the encryption of the message 983472?


# Given values
p = 447106507
q = 5940619
e = 53
m = 983472

# Step 1: Compute n
n = p * q

# Step 2: Compute Euler's totient
phi_n = (p - 1) * (q - 1)

# Step 3: Compute private key d (modular inverse of e mod phi_n)
# Python's pow() with -1 exponent finds modular inverse in Python 3.8+
d = pow(e, -1, phi_n)

# Step 4: Encrypt the message
# Compute ciphertext c = m^e mod n
c = pow(m, e, n)

# Step 5: Print results
print("n =", n)
print("phi(n) =", phi_n)
print("Private key d =", d)
print("Encrypted message =", c)
# Step 6: Decrypt the message

######################################################################################

# Reverse problem: Given p = 97, q = 101, e = 7, and ciphertext c = 253,
# find the private key d and decrypt the message to get the plaintext.

# Given values
p = 97
q = 101
e = 7
c = 253  # ciphertext

# Step 1: Compute modulus n
n = p * q

# Step 2: Compute Euler's totient φ(n)
phi_n = (p - 1) * (q - 1)

# Step 3: Compute private key d (modular inverse of e mod φ(n))
d = pow(e, -1, phi_n)

# Step 4: Decrypt the ciphertext
# Compute plaintext m = c^d mod n
m = pow(c, d, n)

# Step 5: Print all results
print("n =", n)
print("phi(n) =", phi_n)
print("Private key d =", d)
print("Decrypted message =", m)

#############################################################

# Suppose n = pq = 437024078297897179, phi(n) = 437024076975443440, 
# p - q = 28063878. Compute p and q

# double check
p = 675258809
q = 647194931
pn = (p - 1) * (q - 1)
n = p* q
print("phi(n) =", pn)
print("n =", n)
print(p - q)

# solve manually

# expand pn = 437024076975443440
# pn = (p - 1) * (q - 1) =p*q - p - q + 1
# rearrange 
# p + q = p*q - pn + 1
print("p+q =", n - pn + 1)
# solve for p using p+q and p-q
# p-q = 28063878
# p+q = 1322453740
# 2p = 280941378 + 1322453740
# p = (28063878 + 1322453740) / 2
print("p =", (28063878 + 1322453740) / 2)
print("q =", 1322453740 - 675258809)