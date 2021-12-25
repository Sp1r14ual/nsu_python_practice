from math import sqrt
n = int(input())
while n > 2:
    n = sqrt(n)
    print("%.3f" % (n))
