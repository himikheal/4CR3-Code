# Consider an LFSR with coefficients [p_0, ..., p_9] = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0,] and initial value [s_0, ..., s_9] = [0, 0, 1, 0, 0, 1, 0, 1, 0, 0]. Generate the next 10 bits [s_{10}, ..., s_{19}] of the output of this lsfr.

# In AES-128, which of the following correctly describes how round subkeys are generated?
# - A. Each round key is a random 16-byte value chosen independently from the main key

# False, round keys are derived from the main key using a key schedule algorithm.

# - B. The key schedule expands the 128-bit key into 11 round keys using byte rotations, S-box substitution, and round constants (RC[i])

# True, the key schedule for AES-128 expands the main key into 11 round keys using byte rotations, S-box substitutions, and round constants (RC[i]).

# - C. The same 128-bit key is reused for all 10 rounds to ansure consistency

# False, each round uses a different round key derived from the main key.

# - D. The key schedule for AES-128 includes modular multiplication in GF(2^8) using the MixColumns matrix.

# False, modular multiplication in GF(2^8) is used in the MixColumns step, not in the key schedule.