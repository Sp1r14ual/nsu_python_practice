power = int(input())
acc = 1
i = 1
flag = False
while True:
    acc *= 2
    if power == 1 or acc == power:
        print("верно")
        flag = True
        break
    if acc > power:
        break
    i += 1
if not flag:
    print("неверно")

#Говнокод