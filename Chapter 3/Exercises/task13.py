wage = float(input())
count = 0
summa = 0
if wage == 0:
    count += 1
while wage != 0:
    summa += wage
    count += 1
    wage = float(input())
print(summa / count)