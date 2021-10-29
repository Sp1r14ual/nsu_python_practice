import turtle, math

def triangle(a, color):
    '''a - гипотенуза'''
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(a * math.sqrt(2)/2)
    turtle.right(90)
    turtle.forward(a * math.sqrt(2)/2)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(180) 
    turtle.end_fill()
    turtle.up()

def square(a, color):
    '''a - сторона'''
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

def parallelogram(a, b, color):
    '''a - меньшая сторона, b - большая сторона'''
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(180-45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(180)
    turtle.end_fill()
    turtle.up()

def figure1():
    turtle.left(180)
    turtle.setposition(100, 100)
    triangle(200, "red")

    turtle.setposition(-100, 100)
    turtle.left(90)
    triangle(200, "yellow")

    turtle.setposition(100, -0)
    turtle.left(180)
    triangle(100, "orchid")

    turtle.left(135)
    square(50 * math.sqrt(2), "orange")

    triangle(100 * math.sqrt(2), "cyan")

    turtle.left(135)
    turtle.setposition(-50, -50)
    triangle(100, "violet")

    turtle.setposition(-100, -100)
    parallelogram(50 * math.sqrt(2), 100, "lime")





    

figure1()
turtle.exitonclick()