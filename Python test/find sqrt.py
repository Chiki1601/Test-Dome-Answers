from math import sqrt

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    return ( (-b + sqrt(discriminant))/(2*a), (-b - sqrt(discriminant))/(2*a) )

print(find_roots(2, 10, 8));
