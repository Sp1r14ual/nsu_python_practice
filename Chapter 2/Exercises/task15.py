num = int(input())
if (num >= 5 and num <= 14) or num % 10 == 5 or num % 10 == 6 or num % 10 == 7 or num % 10 == 8 or num % 10 == 9 or num % 10 == 0:
    print(str(num),"попугаев")
elif num % 10 == 1:
    print(str(num),"попугай")
elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
    print(str(num),"попугая")