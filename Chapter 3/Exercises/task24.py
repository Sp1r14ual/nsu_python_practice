for i in range(100000, 1000000):
    num = str(i)
    if num[1] == num[5] and num[2] == num[4]:
        if str(int(num) + 1)[1] == str(int(num) + 1)[5] and str(int(num) + 1)[2] == str(int(num) + 1)[4]:
            if str(int(num) + 2)[1] == str(int(num) + 2)[4] and str(int(num) + 2)[2] == str(int(num) + 2)[3]:
                if str(int(num) + 3)[0] == str(int(num) + 3)[5] and str(int(num) + 3)[1] == str(int(num) + 3)[4] and str(int(num) + 3)[2] == str(int(num) + 3)[3]:
                    print(i)
