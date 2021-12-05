from turtle import *
from math import sqrt

x1 = numinput("Координаты центра окружности 1", "Введите xc", 0, minval=-300, maxval=300)
y1 = numinput("Координаты центра окружности 1", "Введите yc", 0, minval=-300, maxval=300)
r1 = numinput("Окружность 1", "Введите радиус r ", 0, minval=0, maxval=300)
x2 = numinput("Координаты центра окружности 2", "Введите xc", 0, minval=-300, maxval=300)
y2 = numinput("Координаты центра окружности 2", "Введите yc", 0, minval=-300, maxval=300)
r2 = numinput("Окружность 1", "Введите радиус r ", 0, minval=0, maxval=300)

up()
setposition(x1, y1 - r1)
down()
circle(r1)
up()
setposition(x2, y2 - r2)
down()
circle(r2)

d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if r1 + r2 < d:
    print("Окружности лежат одна вне другой, не касаясь")
if r1 + r2 > d and r1 + d > r2 and r2 + d > r1:
    print("Окружности пересекаются")
if r1 + r2 == d:
    print("Окружности имеют внешнее касание")
if abs(r1 - r2) == d:
    print("Окружности имеют внутреннее касание; ")
if r1 + d < r2 or r2 + d < r1:
    print("Одна окружность лежит внутри другой, не касаясь.")

exitonclick()