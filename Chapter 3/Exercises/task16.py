n = int(input())
for i in range(1, n + 1):
    stars = i
    for j in range(n):
        if j < n - stars:
            print(" ", end="")
        else:
            print("*", end="")
    print()
