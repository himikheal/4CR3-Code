def phi(n):
    result = n
    p = 2
    
    while p * p <= n:
        if n % p == 0:
            # subtract multiples of p
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    # If n is a prime greater than 1
    if n > 1:
        result -= result // n
    
    return result

# Example:
print(phi(952))   # should output 384