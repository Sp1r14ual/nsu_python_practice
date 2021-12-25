flag = False 
while not flag:
    number = int(input())
    for i in range(number + 1):
        if i ** 2 == number:
            print("да")
            flag = True
    else:
        print("введите другое число")





#Nope