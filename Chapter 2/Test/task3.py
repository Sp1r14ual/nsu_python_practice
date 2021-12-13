a = int(input())
b = int(input())
r = int(input())
m = int(input())

long = a if a >= b else b
short = a if a <= b else b

minimum_to_short_wall = m if m <= long - m else long - m
minimum_to_long_wall = r if r <= short - r else short - r

print(minimum_to_long_wall if minimum_to_long_wall <= minimum_to_short_wall else minimum_to_short_wall)
