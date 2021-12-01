a = input()

if ((a[0] == "a" or a[0] == "c" or a[0] == "e" or a[0] == "g") and int(a[1]) % 2 == 1) or ((a[0] == "b" or a[0] == "d" or a[0] == "f" or a[0] == "h") and int(a[1]) % 2 == 0):
    print("черный")
else:
    print("белый")