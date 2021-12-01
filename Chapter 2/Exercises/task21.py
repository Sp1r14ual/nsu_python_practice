from math import sqrt
d = 6.5 * 2
a, b = map(float, input().split("x"))
d1 = sqrt(a ** 2 + b ** 2)
if d1 > d:
    print("нет")
else:
    print("да")