result = int(input())
maximum = -1
count = 0
while result != -1:
    if result > maximum:
        maximum = result
    count += 1
    result = int(input())

#print(maximum)
#print(count)

#Раскомментируйте соответствующий print()