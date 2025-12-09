"""
Given p and q, find valid DSA generator (beta) among candidates
"""

# p = 899009829279928687167847647253
# q = 5938170550372221380503

p = 2089
q = 29

# candidates = {
#     "A": 428025207316609689260868108104,
#     "B": 511817553315794935894966990404,
#     "C": 52741071529976599941769481354,
#     "D": 430222494411980041758424435195,
# }

candidates = {
    "A": 774,
    "B": 1762,
    "C": 1189,
    "D": 512,
}

valid = []
for name, beta in candidates.items():
    # test subgroup membership: beta^q mod p == 1
    if pow(beta, q, p) == 1 and 1 < beta < p - 1:
        valid.append(name)

print("Valid candidate(s):", valid)

