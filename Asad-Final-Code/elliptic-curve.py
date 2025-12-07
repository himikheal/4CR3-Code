def is_elliptic(a, b, p):
    return (4 * pow(a, 3) + 27 * pow(b, 2)) % p != 0

def add_points(a, b, p, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    if x1 == x2 and y1 == y2:
        s = (3 * pow(x1, 2) + a) * pow(2 * y1, -1, p) % p
    else:
        s = (y2 - y1) * pow(x2 - x1, -1, p) % p
    
    x3 = (pow(s, 2) - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3

def calculate_curve_order(base_point, a, b, p):
    current = base_point
    order = 1
    
    while True:
        try:
            current = add_points(a, b, p, current, base_point)
            order += 1
            if current == base_point:  # Back to original point
                return order + 1
        except:  # Point at infinity reached
            return order + 1

def calculate_point_order(a, b, p, point, curveOrder):
    x, y = point
    temp = point

    if (pow(y, 2) % p != (pow(x, 3) + a*x + b) % p):
        return -1 # point is not on curve
    
    for i in range(1, curveOrder -1):
        try:
           print(temp)
           temp = add_points(a, b, p, point1=point, point2=temp)
        except:
            return i + 1
        
    return -2

def elliptic_curve_order(a, b, p):
    def is_point_on_curve(x, y):
        # Check if point satisfies y^2 ≡ x^3 + ax + b (mod p)
        return (y**2) % p == (x**3 + a * x + b) % p

    count = 1  # Include point at infinity
    
    # Check all possible x,y coordinates modulo p
    for x in range(p):
        for y in range(p):
            if is_point_on_curve(x, y):
                count += 1

    return count

print(is_elliptic(1, 2, 11))
print(add_points(1, 2, 11, (8, 4), (8, 4)))
print(elliptic_curve_order(2, 2, 17))
print(calculate_point_order(1, 2, 11, (10,0), 16))