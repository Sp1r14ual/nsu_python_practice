pin = int(input())
flag = True

if len(str(pin)) != 4:
    flag = False

for i in range(0, len(str(pin)) - 1):
    for j in range(i + 1, len(str(pin))):
        if str(pin)[i] == str(pin)[j]:
            flag = False

if pin >= 1900 and pin <= 2050:
    flag = False

if flag:
    print("OK")
else:
    print("ERROR")