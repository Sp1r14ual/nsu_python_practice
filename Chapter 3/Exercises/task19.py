n = int(input())
for i in range(2, n + 1):
    is_complicated = False
    for j in range(2, i):
        if i % j == 0:
            is_complicated = True
            break
    if not is_complicated:
        print(i)
