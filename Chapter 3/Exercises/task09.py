n, k, r = map(int, input().split())
day = 1
while n < r:
    n *= (1 + k / 100)
    day += 1
print(day)