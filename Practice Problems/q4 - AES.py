# Which of the following statements are true regarding AES:
# (a) It is a bit-oriented cipher.

# False
# AES is a byte-oriented cipher, meaning it processes data in 8-bit (1 byte) chunks rather than individual bits.

# (b) It has fast software implementations.

# True
# Modern block ciphers are now very fast

# (c) The Diffusion Layer is not invertible.

# False
# The diffusion layer is fully invertible

# (d) The number of rounds depends on the key size.

# True
# Number of rounds nr = 10 or 12 or 14 based on key size

# (e) The arithmetic in AES, such as multiplication, is integer arithmetic.

# False
# All arithmetic is done in the Galois field Gal(28)

# (f) There are no known subexponential attacks against AES.

# True
# THere are no known subexponential attacks against AES.






# Overview of AES
# • AES is not a Feistel network
# • Number of rounds nr = 10 or 12 or 14 based on key size
# • Each round consists of layers

# Internal Structure of AES
# • AES is a byte-oriented cipher
# • The input of AES can be arranged in a 4 × 4 matrix
# A =
# A0 A4 A8 A12
# A1 A5 A9 A13
# A2 A6 A10 A14
# A3 A7 A11 A15
# where each Aj is a byte, and A0, A1, . . . , A15 is the 16-byte input of AES.
# • AES operates on a 4 × 4 matrix like this, called the data state, throughout its exectution.

# Byte Substitution Layer ->
# ShiftRows Layer ->
# MixColumn Layer