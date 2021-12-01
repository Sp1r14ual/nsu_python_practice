a, b = map(int, input().split("x"))
c, d, e = map(int, input().split("x"))

if (a >= c and b >= d) or (a >= d and b >= c) or (a >= c and b >= e) or (a >= e and b >= c) or (a >= d and b >= e) or (a >= e and b >= d):
    print("да")
else:
    print("нет")

