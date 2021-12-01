k = int(input())
if k % 5 == 0 or k % 7 == 0:
    print("да")
    exit()
else:
    for i in range(k // 2):
        for j in range(k // 2):
            if i * 5 + j * 7 == k:
                print("да")
                exit()
print("нет")
