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


#Person by the right from the square on preview
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

#Person by the left from the square on preview
def figure3():
    #Change parameter below to change painting's size
    a = 400
    #Change parameter above to change painting's size

    turtle.left(45)
    triangle(a, "red")

    turtle.setposition(1/4 * a/2 * math.sqrt(2), a/2 * math.sqrt(2))
    turtle.left(90)
    square(a/4, "orange")
    
    turtle.setposition(0, a/2 * math.sqrt(2))
    turtle.left(90)
    parallelogram(a/4 * math.sqrt(2), a/2, "lime")

    turtle.setposition(1/4 * a/2 * math.sqrt(2), 1/4 * a/2 * math.sqrt(2))
    triangle(a, "yellow")

    turtle.setposition(1/4 * a/2 * math.sqrt(2), -1/2 * a/2 * math.sqrt(2))
    turtle.left(45)
    triangle(a/2, "cyan")

    turtle.setposition(1/4 * a/2 * math.sqrt(2), -1/2 * a/2 * math.sqrt(2) - 9/10 * a/2 * math.sqrt(2))
    turtle.left(180)
    triangle(a/4, "violet")

    turtle.setposition(9/10 * (-3/4 * a/2 * math.sqrt(2) - a/4 * math.sqrt(2)/2), 9/10 * (-3/4 * a/2 * math.sqrt(2) - a/4 * math.sqrt(2)/2))
    turtle.right(45)
    triangle(a/4, "orchid")

#ship
def figure4():
    #Change parameter below to change painting's size
    a = 300
    #Change parameter above to change painting's size
    turtle.setposition(0, a)
    turtle.right(90)
    triangle(a, "red")

    turtle.setposition(a/2, a/2)
    turtle.left(45)
    square(a/4 * math.sqrt(2), "orange")

    turtle.setposition(0, 0)
    turtle.left(45)
    triangle(a/2, "orchid")

    turtle.setposition(a/4 * math.sqrt(2), a)
    turtle.left(135)
    triangle(a/2, "violet")

    turtle.setposition(a/2, 0)
    turtle.left(45)
    triangle(3/4 * a, "cyan")

    turtle.setposition(0, a * 1/10 + a * math.sqrt(2)/2)
    turtle.left(45)
    triangle(a, "yellow")

    turtle.setposition(-5/8 * a, 0)
    turtle.left(90)
    parallelogram(a/2 * 3/4, 3/4 * a * math.sqrt(2)/2, "lime")

def figure5():
    turtle.setposition(100, -100)
    turtle.left(90)
    triangle(200, "yellow")

    turtle.setposition(100, 100)
    turtle.left(180)
    triangle(200, "red")

    turtle.setposition(-50, 100)
    turtle.left(90)
    triangle(150, "cyan")

    turtle.setposition(100, 100)
    parallelogram(50 * math.sqrt(2), 100, "lime")

    turtle.setposition(-50, -50)
    triangle(100, "orchid")

    turtle.setposition(0, 0)
    turtle.left(180)
    triangle(100, "violet")

    turtle.setposition(-100, 0)
    turtle.left(45)
    turtle.forward(25)
    turtle.right(90)
    square(50, "orange")














turtle.speed("fast")

#figure1()
#figure2()
#figure3()
#figure4()
figure5()
turtle.exitonclick()