floors_per_entrance = int(input())
flats_per_floor = int(input())
flat_number = int(input())

if flat_number % (floors_per_entrance * flats_per_floor) == 0:
    entrance = flat_number // (floors_per_entrance * flats_per_floor)
    floor = floors_per_entrance
else:
    entrance = flat_number // (floors_per_entrance * flats_per_floor) + 1
    rest = flat_number % (floors_per_entrance * flats_per_floor)

    floor =  rest // flats_per_floor + int(bool(rest % flats_per_floor))

print(entrance, floor)