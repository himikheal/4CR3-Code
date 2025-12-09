import random

def bits_from_bytes(b):
    """Convert bytes to list of bits."""
    bits = []
    for byte in b:
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)
    return bits

def bytes_from_bits(bits):
    """Convert list of bits back to bytes."""
    if len(bits) % 8 != 0:
        raise ValueError("Number of bits must be a multiple of 8")
    out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        out.append(byte)
    return bytes(out)

def generate_keystream_bits(n, seed=None):
    """Generate n-bit keystream."""
    rng = random.Random(seed)
    ks = []
    for _ in range(n):
        ks.append(rng.getrandbits(1))
    return ks

def stream_encrypt_bits(plaintext_bits, keystream_bits):
    """Encrypt by XOR."""
    ciphertext = []
    for i in range(len(plaintext_bits)):
        ciphertext.append((plaintext_bits[i] ^ keystream_bits[i]))
    return ciphertext

def stream_decrypt_bits(cipher_bits, keystream_bits):
    """Decrypt (same XOR)."""
    plaintext_bits = []
    for i in range(len(cipher_bits)):
        plaintext_bits.append(cipher_bits[i] ^ keystream_bits[i])
    return plaintext_bits

# ---------------- DEMO ----------------

plaintext_text = "HELLO, world!"
print("Plaintext:", plaintext_text)

# Convert plaintext to bits
plain_bytes = plaintext_text.encode("utf-8")
plain_bits = bits_from_bytes(plain_bytes)

# Generate keystream
keystream_bits = generate_keystream_bits(len(plain_bits), seed=42)

# Encrypt
cipher_bits = stream_encrypt_bits(plain_bits, keystream_bits)

# Convert ciphertext to hex for display
cipher_bytes = bytes_from_bits(cipher_bits)
print("Encrypted (hex):", cipher_bytes.hex())

# Decrypt
decrypted_bits = stream_decrypt_bits(cipher_bits, keystream_bits)
decrypted_bytes = bytes_from_bits(decrypted_bits)
print("Decrypted:", decrypted_bytes.decode("utf-8"))



# Show some sample bits
print("\nFirst 32 plaintext bits: ", plain_bits[:32])
print("First 32 keystream bits:", keystream_bits[:32])
print("First 32 cipher bits:   ", cipher_bits[:32])
