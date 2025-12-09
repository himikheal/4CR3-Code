def is_generator(g, p):
    for i in range(1, p - 1):
        if pow(g, i, p) == 1:
            return False
    return True


# def is_generator(g, p):
#     n = p - 1
#     factors = set()
#     d = 2
#     while d * d <= n:
#         while n % d == 0:
#             factors.add(d)
#             n //= d
#         d += 1
#     if n > 1:
#         factors.add(n)

#     # check generator condition
#     for q in factors:
#         if pow(g, (p - 1) // q, p) == 1:
#             return False
#     return True


print(is_generator(602, 953))
print(is_generator(746, 953))
print(is_generator(780, 953))
print(is_generator(94, 953))
