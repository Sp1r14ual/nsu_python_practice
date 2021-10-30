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


#Square built of other figures
def figure1():
    #Change parameter below to change size
    a = 500
    #Change parameter above to change size

    turtle.left(180)
    turtle.setposition(a / 2, a / 2)
    triangle(a, "red")

    turtle.setposition(-(a / 2), (a / 2))
    turtle.left(90)
    triangle(a, "yellow")

    turtle.setposition(a / 2, 0)
    turtle.left(180)
    triangle(a / 2, "orchid")

    turtle.left(135)
    square(a / 2 * math.sqrt(2) / 2, "orange")

    triangle(a / 2 * math.sqrt(2), "cyan")

    turtle.left(135)
    turtle.setposition(-(a / 4), -(a / 4))
    triangle(a / 2, "violet")

    turtle.setposition(-(a / 2), -(a / 2))
    parallelogram(a / 2 * math.sqrt(2) / 2, a / 2, "lime")


#Person 2
def figure2():
    #Change parameter below to change painting's size
    a = 400
    #Change parameter above to change painting's size

    turtle.left(45)
    triangle(a, "yellow")

    turtle.setposition(-(a / 2) * math.sqrt(2), a / 2 * math.sqrt(2))
    turtle.right(90)
    triangle(a, "red")

    turtle.setposition(0, (a / 2) * math.sqrt(2))
    turtle.left(180)
    square(a / 4, "orange")

    turtle.setposition(a / 4 * math.sqrt(2), -(a / 4) * math.sqrt(2))
    triangle(a / 2, "cyan")

    turtle.setposition(a / 4 * math.sqrt(2) * 3/4, -(a / 4) * math.sqrt(2))
    turtle.right(180)
    triangle(3/4 * (a / 2), "violet")

    turtle.setposition(0, 0)
    turtle.right(90)
    parallelogram(a / 4 * math.sqrt(2) * 3/4, a / 4 * math.sqrt(2), "lime")

    turtle.setposition(-(a * 65/1000) * math.sqrt(2), -(a / 4) * math.sqrt(2))
    triangle((a / 2) * 3/4, "orchid")

turtle.speed("fast")

#figure1()
figure2()
turtle.exitonclick()