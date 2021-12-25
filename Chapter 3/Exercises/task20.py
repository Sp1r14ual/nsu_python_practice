n = int(input())
for i in range(6, n + 1):
    summa = 0
    for j in range(1, i // 2 + i % 2 + 1):
        if i % j == 0:
            summa += j
    if summa == i:
        print(i)
