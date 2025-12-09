# Suppose h : {0, 1}^∗ → {0, 1}^n hash function that is preimage resistant and pseudorandom,
# i.e., the distribution of the output of h is close to uniform.
# Let n = 128, so the output of h is 16 bytes. 
# We are looking for an input x such that the third 32 bits of h(x) are 11100011100100011001011100110011.
# In other words, we seek x such that h(x) = y, where y = ab11100011100100011001011100110011d,
# and a, b, and d are arbitrary 32-bit strings.
# How many inputs, in the worst case, would we need to try to find such a y?

# Since h is preimage resistant and pseudorandom, we can assume that the output of h is uniformly distributed.
# The output of h is 128 bits long, and we are looking for a specific pattern in the third 32 bits.
# The probability of randomly guessing the correct 32 bits is 1 in 2^32, since there are 2^32 possible combinations of 32 bits.

# Therefore, in the worst case, we would need to try 2^32 different inputs to find an input x such that h(x) has the desired pattern in the third 32 bits.