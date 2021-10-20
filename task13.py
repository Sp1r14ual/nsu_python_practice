from math import pi

r1 = int(input())
r2 = int(input())
if r1 >= r2:
    print(pi*r1*r1 - pi*r2*r2)
else:
    print(pi*r2*r2 - pi*r1*r1)

