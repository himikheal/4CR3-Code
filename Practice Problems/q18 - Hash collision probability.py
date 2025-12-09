# Let h : {0, 1}* → {0, 1}^100 be a preimage resistant hash function.
# Suppose you have a machine M that can compute 2^30 hashes per second.
# Using M, approximately how long does it take to find a collision,
# with probability at least 1/2, for h?
# (a) 35 million years
# (b) 15 days
# (c) 1 year
# (d) 10 years

# It takes approvimately 15 days to find a collision with probability at least 1/2 for h.


import math

def birthday(n, p = 0.5):
    return pow(2, (n+1)/2) * math.sqrt(-1*math.log(1-p))

def birthday_calc(n, lambda_prob):
    t = 2**((n + 1) / 2) * math.sqrt(-math.log(1 - lambda_prob))
    return t

messages = birthday_calc(100, 0.5)
print("Messages needed to be checked:")
print(messages)
# double verify
print(birthday(100))

# M can compute 2^30 hashes per second
# messages / (2^30) = seconds
print("Seconds needed to find a collision:")
seconds = messages / (2**30)
print(seconds)
print("hours:")
print(seconds / 3600)
print("days:")
print(seconds / 3600 / 24)


# t is the amount of messages we need to try to find a collision
# (with probability at least (λ*100)%) in a hash function with an n-bit output
# t ≈ 2^((n+1)/2) * sqrt(-ln(1 − λ))
# 
# To find a collision (with probability at least 50%) in a hash function with an 80-bit output, 
# we need to try
# t = 2^((80+1)/2) * sqrt(-ln(1 − 0.5)) ≈ 240.2 messages
