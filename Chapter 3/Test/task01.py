x = int(input())
summa = 0
count = 0
for i in range(1, x+1):
    summa += i
    count += 1
    if summa % count == 0:
        print(summa)
