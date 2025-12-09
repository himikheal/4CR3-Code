# Consider the affine cipher with m=26, where the alphabet is A=0, B=1, C=2, etc
# Given the plaintext "HELLO" and the corresponding ciphertext "RCLLA", find the key (a, b)

# Affine Cipher
# Transform each symbol by a linear map
# • Key: a, b ∈ Z_m, where a is invertible mod m
# • Plaintext: x ∈ Z_m
# • Ciphertext: y ∈ Z_m
# Encryption: e_k(x) ≡ ax + b mod m
# Decryption: d_k(y) ≡ a_inv(y − b) mod m

# Example: the alphabet
# • m = 26
# • Key: (a, b) = (9, 13), where a_inv ≡ 3 mod 26
# Palintext: attack = 0, 19, 19, 0, 2, 10.
# Ciphertext: 13, 2, 2, 13, 5, 25 = nccnfz

plaintext = "HELLO"
ciphertext = "RCLLA"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_affine_key(plaintext, ciphertext):
    m = 26
    p_nums = [ord(c) - ord('A') for c in plaintext]
    c_nums = [ord(c) - ord('A') for c in ciphertext]

    for a in range(1, m):
        if gcd(a, m) != 1:
            continue
        for b in range(m):
            if all((a * p + b) % m == c for p, c in zip(p_nums, c_nums)):
                return (a, b)
    return None

key = find_affine_key(plaintext, ciphertext)
print("The key (a, b) is:", key)

def encrypt_affine(plaintext, a, b):
    m = 26
    ciphertext = ""
    for char in plaintext:
        x = ord(char) - ord('A')
        y = (a * x + b) % m
        ciphertext += chr(y + ord('A'))
    return ciphertext

encrypted_text = encrypt_affine(plaintext, key[0], key[1])
print("Encrypted text is:", encrypted_text)
print("Ciphertext matches:", encrypted_text == ciphertext)

def decrypt_affine(ciphertext, a, b):
    m = 26
    a_inv = pow(a, -1, m)
    plaintext = ""
    for char in ciphertext:
        y = ord(char) - ord('A')
        x = (a_inv * (y - b)) % m
        plaintext += chr(x + ord('A'))
    return plaintext

decrypted_text = decrypt_affine(ciphertext, key[0], key[1])
print("Decrypted text is:", decrypted_text)
print("Plaintext matches:", decrypted_text == plaintext)