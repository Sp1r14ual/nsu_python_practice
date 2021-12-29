flag = False 
while not flag:
    number = int(input())
    if number == 1:
        print("является полным квадратом")
        flag = True
    else:
        for i in range(number // 2 + number % 2 + 1):
            if i ** 2 == number:
                print("является полным квадратом")
                flag = True

    if not flag:
        print("не является полным квадратом")