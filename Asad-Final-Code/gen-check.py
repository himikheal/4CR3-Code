from sympy.ntheory import divisors, isprime

# g = 42504424932574pip 8129860331117047
# p = 899009829279928687167847647253
# l = [2,3,47,89477,5938170550372221380503]

g = 780
p = 953
l = divisors(p-1)
primeDiv = set()
for i in l:
    if isprime(i):
        primeDiv.add(i)

print(primeDiv)

bool = True
for i in primeDiv: 
    if (pow(g, (int) (( p-1)//i), p) == 1):
        print(i)
        bool = False

print(bool)


# print(pow(g, (int) (( p-1)/3), p))
# print(pow(g, (( p-1)//3), p))

# num = 299669943093309562389282549084

# print(pow(g, num, p))
# print((int) (( p-1)/3))
# print((( p-1)//3))
# print(299669943093309562389282549084 * 3)
