# Define the original alphabet and the substitution permutation (the key)
alphabet = "abcdefghijklmnopqrstuvwxyz,‘;.?"
permutation = "yeqjul’wsrpifxthm.zk,d;voabg?c n"

# Build encryption and decryption dictionaries
encrypt_dict = {a: p for a, p in zip(alphabet, permutation)}
decrypt_dict = {p: a for a, p in zip(alphabet, permutation)}

def encrypt(message):
    return ''.join(encrypt_dict.get(c, c) for c in message)

def decrypt(message):
    return ''.join(decrypt_dict.get(c, c) for c in message)

# Example
plaintext = "information"
ciphertext = encrypt(plaintext)
decrypted = decrypt(ciphertext)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)