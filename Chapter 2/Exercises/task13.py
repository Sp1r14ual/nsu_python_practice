from turtle import *
from math import sqrt
# Ввод данных
# с использованием диалоговых окон
xc = numinput("Координаты центра окружности", "Введите xc", 0, minval=-300, maxval=300)
yc = numinput("Координаты центра окружности", "Введите yc", 0, minval=-300, maxval=300)
r = numinput("Окружность", "Введите радиус r ", 0, minval=0, maxval=300)
x = numinput("Координаты точки", "Введите x", 0, minval=-300, maxval=300)
y = numinput("Координаты точки", "Введите y", 0, minval=-300, maxval=300)

penup()
setposition(xc, yc - r)
pendown()
circle(r)
penup()
setposition(x, y)
pendown()
dot("red")

penup()
hideturtle()

if r < sqrt((x - xc) ** 2 + (y - yc) ** 2):
    print("Точка вне окружности")
elif r > sqrt((x - xc) ** 2 + (y - yc) ** 2):
    print("Точка внутри окружности")
else:
    print("Точка лежит на окружности")

exitonclick()

