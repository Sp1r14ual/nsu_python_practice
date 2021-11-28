number = int(input())
if number // 1000 == number % 10 and (number // 100) % 10 == (number % 100) // 10:
    print("настоящее")
else:
    print("кривое")