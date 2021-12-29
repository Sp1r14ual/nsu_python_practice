high = int(input())
low = 1
steps = 0

while low < high:
    high = (low + high) // 2
    steps += 1

print(steps)

#см. бинарный поиск в книге "Грокаем алгоритмы"