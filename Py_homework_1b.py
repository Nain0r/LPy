import math

a = 1
b = 5
c = 4

discriminant = b**2 - 4*a*c
root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)

print(f"x1 = {root1} and x2 = {root2}")
