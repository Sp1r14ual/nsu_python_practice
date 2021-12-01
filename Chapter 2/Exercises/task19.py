knat = int(input())

sikl = knat // 29
knat -= sikl * 29

galleon = sikl // 17
sikl -= galleon * 17

if galleon == 0 and sikl == 0:
    print(knat,"кнатов")
elif galleon == 0 and sikl != 0 and knat != 0:
    print(sikl,"сиклей")
    print(knat,"кнатов")
elif galleon != 0 and sikl == 0 and knat != 0:
    print(galleon,"галлеонов")
    print(knat,"кнатов")
elif galleon != 0 and sikl != 0 and knat == 0:
    print(galleon,"галлеонов")
    print(sikl,"сиклей")
elif galleon != 0 and sikl == 0 and knat == 0:
    print(galleon,"галлеонов")
elif galleon == 0 and sikl != 0 and knat == 0:
    print(sikl,"сиклей")
else:
    print(galleon,"галлеонов")
    print(sikl,"сиклей")
    print(knat,"кнатов")


