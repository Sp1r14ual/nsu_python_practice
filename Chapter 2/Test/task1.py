num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10

maximum = int()
middle = int()
minimum = int()

if a > b and a > c:
    maximum = a
    middle = b if b > c else c
    minimum = c if middle == b else b
elif b > a and b > c:
    maximum = b
    middle = a if a > c else c
    minimum = c if middle == a else a
elif c > a and c > b:
    maximum = c
    middle = a if a > b else b
    minimum = a if middle == b else b

print("ДОСМОТРЕТЬ" if (maximum + minimum) // 2 == middle else "ПРОПУСТИТЬ")

