t = -1
prev = -1
count = 0
t = float(input())
while t != 0:
    if t < prev:
        count += 1
    prev = t
    t = float(input())
print(count)
