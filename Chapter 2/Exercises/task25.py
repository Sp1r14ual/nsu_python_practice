start, finish = map(str, input().split("-"))
if chr(ord(start[0]) + 2) == finish[0] and int(start[1]) - 1 == int(finish[1]):
    print("верно")
elif chr(ord(start[0]) + 2) == finish[0] and int(start[1]) + 1 == int(finish[1]):
    print("верно")
elif chr(ord(start[0]) + 1) == finish[0] and int(start[1]) + 2 == int(finish[1]):
    print("верно")
elif chr(ord(start[0]) - 1) == finish[0] and int(start[1]) + 2 == int(finish[1]):
    print("верно")
elif chr(ord(start[0]) - 2) == finish[0] and int(start[1]) + 1 == int(finish[1]):
    print("верно")
elif chr(ord(start[0]) - 2) == finish[0] and int(start[1]) - 1 == int(finish[1]):
    print("верно")
elif chr(ord(start[0]) - 1) == finish[0] and int(start[1]) - 2 == int(finish[1]):
    print("верно")
elif chr(ord(start[0]) + 1) == finish[0] and int(start[1]) - 2 == int(finish[1]):
    print("верно")
else:
    print("ошибка")

#Да, я больной ублюдок