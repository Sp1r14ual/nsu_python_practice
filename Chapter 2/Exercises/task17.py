year1 = int(input())
year2 = int(input())
year3 = int(input())

if year1 == year2 and year1 == year3:
    print(3)
elif (year1 == year2 and not year1 == year3) or (not year1 == year2 and year1 == year3) or (year2 == year1 and not year2 == year3) or (not year2 == year1 and year2 == year3) or (year3 == year1 and not year3 == year2) or (not year3 == year1 and year3 == year2):
    print(2)
else:
    print(0)