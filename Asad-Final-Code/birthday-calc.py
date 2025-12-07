import math

def birthday(n, p = 0.5):
    return pow(2, (n+1)/2) * math.sqrt(-1*math.log(1-p))

print(birthday(100) / pow(2,30) / 3600)