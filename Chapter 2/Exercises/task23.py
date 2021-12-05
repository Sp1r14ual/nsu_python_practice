a, b = map(int, input().split("x"))
c = int(input())
s = a * b
if (c % a == 0 or c % b == 0) and s > c:
    print("успешно")
else:
    print("неосуществимо")