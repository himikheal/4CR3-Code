# Let S = (Gen, Sig, Ver) be a signature scheme that is existentially unforgeable.
# Recall that in an existential forgery attack, the attacker constructs a new message-signature pair (m, s), 
# where m has never been previously signed by the legitimate signer.
# Consider the following new signature scheme S′ = (Gen, Sig′, Ver′) based on S,
# where Sig′ and Ver′ are defined as follows:
# - Sig′(m, k_pr): 
#       Choose a random r ← {0, 1}^n,
#       output (r, Sig(k_pr, m ⊕ r), Sig(k_pr, r)).
# - Ver′(m, k_pub, (r, s1, s2)):
#       Output “accept” if and only if
#       Ver(k_pub, m ⊕ r, s1) = Ver(k_pub, r, s2) = “accept”.
# Is S′ a secure signature scheme? If so, justify your answer; otherwise, give an attack.



# Assume the attacker has a signature (r_a, s1_a, s2_a) for some message m_a
# That is:
# s1_a = Sig(k_pr, m_a ⊕ r_a)
# s2_a = Sig(k_pr, r_a)
# as well as a signature (r_b, s1_b, s2_b) for some message m_b, where
# s1_b = Sig(k_pr, m_b ⊕ r_b)
# s2_b = Sig(k_pr, r_b)

# The attacker can create a message m =
# M = m_a ⊕ r_a ⊕ r_b

# Say we use M and r_b in the valid verification:
# Ver′(k_pub, M, (r_b, x1, x2))
# x1 would need to be Sig(k_pr, M ⊕ r_b)
# x2 would need to be Sig(k_pr, r_b)
# Thus, the verification would be:
# Ver′(k_pub, M, (r_b, Sig(k_pr, M ⊕ r_b), Sig(k_pr, r_b)))
# and verification would check:
# Ver′(k_pub, M ⊕ r_b, Sig(k_pr, M ⊕ r_b)) = Ver′(k_pub, r_b, Sig(k_pr, r_b))

# As long as we can show that:
# Sig(k_pr, M ⊕ r_b) is a valid signature using Sig
# Sig(k_pr, r_b) is a valid signature using Sig
# Then we have created a valid message-signature pair (M, (r_b, Sig(k_pr, M ⊕ r_b), Sig(k_pr, r_b)))

# Since M = m_a ⊕ r_a ⊕ r_b
# M ⊕ r_b = m_a ⊕ r_a
# Thus we have
# Sig(k_pr, M ⊕ r_b) = Sig(k_pr, m_a ⊕ r_a)
# by definition, this is s1_a, which is valid
# Similarly, Sig(k_pr, r_b) is s2_b, which is also valid
# Therefore, we have created a valid message-signature pair
# (M, (r_b, Sig(k_pr, M ⊕ r_b), Sig(k_pr, r_b)))
# or
# (M, (r_b, s1_a, s2_b))

# The attacker has created a new message-signature pair (M, (r_b, s1_a, s2_b)),
# where M has never been previously signed by the legitimate signer.
