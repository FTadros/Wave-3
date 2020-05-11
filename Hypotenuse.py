from math import sqrt
def hyp(a, b):
    c = sqrt(a**2 + b**2)
    return round(c, 2)


a = int(input('Input first side of the right triangle:'))
b = int(input('Input second side of the right triangle: '))

print ('The hypotenuse is:', hyp(a, b))