start = ""
for i in range(9, 1, -1):
    start += str(i)
    print(start + " * 9 + " + str(i - 2) + " = " + str(int(start) * 9 + i - 2))