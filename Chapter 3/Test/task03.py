count = 0
c = int(input())
for a in range(c - 1):
    for b in range(a, c + 1):
        if c == a ** 2 + b ** 2:
            count += 1
print(count)