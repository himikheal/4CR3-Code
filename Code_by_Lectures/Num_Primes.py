from sympy import primerange 

start, end = 2, 953
primes = list(primerange(start, end + 1))
print(f"Number of primes up to {end}:", len(primes))
print(f"Primes between {start} and {end}:", primes)