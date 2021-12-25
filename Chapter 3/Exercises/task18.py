start = ""
for i in range(1, 10):
    start += str(i)
    print(start + " * 8 + " + str(i) + " = " + str(int(start) * 8 + i))

print()
start = ""
for i in range(1, 10):
    start += str(i)
    print(start + " * 9 + " + str(i + 1) + " = " + str(int(start) * 9 + i + 1))

print()
start = ""
for i in range(9):
    start += "1"
    print(start + " * " + start + " = " + str(int(start) * int(start)))
    