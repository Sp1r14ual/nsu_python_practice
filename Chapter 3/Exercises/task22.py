n = int(input())
maximum = 0
for i in range(1, n // 2 + 1):
    if n % i == 0 and i > maximum:
        maximum = i 
print(n // maximum)
