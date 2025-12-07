import gmpy2

n = 508281196310201376192554864656699346831575429768465482788715190735760361687281737746563113895010157
e = 7
y = 4066488477440339689911514138508998613662966982287543919056006242924596335364286584668317646217011

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


print ("e-th root of y:", find_invpow(y, e))
print ("gmpy2 e-th root of y:", gmpy2.iroot(y, e))
print ("equal?", find_invpow(y, e) == gmpy2.iroot(y, e)[0])

# def brute_force_find_x(n, e, y):
#     found = False
#     while not found:
#         new_x = 1
#         if pow(new_x, e, n) == y:
#             found = True
#         else:
#             new_x += 1
    
#     return new_x

# print("Brute forcing x...")
# found_x = brute_force_find_x(n, e, y)
# print("x found:", found_x)
# print("is found x = original x?", found_x == x)