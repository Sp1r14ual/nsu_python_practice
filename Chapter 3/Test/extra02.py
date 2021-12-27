l = list(map(int, input().split(",")))
if len(set(l)) == 1:
    print(1)
elif len(set(l)) == 2:
    counts = []
    for set_item in set(l):
        counts.append(l.count(set_item))
    if (counts[0] == 3 and counts[1] == 2) or (counts[0] == 2 and counts[1] == 3):
        print(3)
    elif (counts[0] == 2 and counts[1] == 2):
        print(5)
elif len(set(l)) == 3:
    counts = []
    for set_item in set(l):
        counts.append(l.count(set_item))
    if (counts[0] == 3 and counts[1] == 1 and counts[2] == 1) or (counts[0] == 1 and counts[1] == 3 and counts[2] == 1) or (counts[0] == 1 and counts[1] == 1 and counts[2] == 3):
        print(4)
    elif (counts[0] == 1 and counts[1] == 2 and counts[2] == 2) or (counts[0] == 2 and counts[1] == 1 and counts[2] == 2) or (counts[0] == 2 and counts[1] == 2 and counts[2] == 1):
        print(5)
elif len(set(l)) == 4:
    print(2)
else:
    print(7)