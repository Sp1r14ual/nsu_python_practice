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
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(180)
    turtle.end_fill()
    turtle.up()


#Square built of other figures
def figure1(x, y, a):

    turtle.up()
    turtle.left(180)
    turtle.setposition(x + a / 2, y + a / 2)
    triangle(a, "red")

    turtle.setposition(x + (-(a / 2)), y + (a / 2))
    turtle.left(90)
    triangle(a, "yellow")

    turtle.setposition(x + a / 2, y + 0)
    turtle.left(180)
    triangle(a / 2, "orchid")

    turtle.left(135)
    square(a / 2 * math.sqrt(2) / 2, "orange")

    triangle(a / 2 * math.sqrt(2), "cyan")

    turtle.left(135)
    turtle.setposition(x + (-(a / 4)), y + (-(a / 4)))
    triangle(a / 2, "violet")

    turtle.setposition(x + (-(a / 2)), y + (-(a / 2)))
    parallelogram(a / 2 * math.sqrt(2) / 2, a / 2, "lime")


#Person by the right from the square on preview
def figure2(x, y, a):

    turtle.up()
    turtle.setposition(x + 0, y + 0)
    turtle.left(45)
    triangle(a, "yellow")

    turtle.setposition(x + (-(a / 2) * math.sqrt(2)),y + (a / 2 * math.sqrt(2)))
    turtle.right(90)
    triangle(a, "red")

    turtle.setposition(x + 0, y + (a / 2) * math.sqrt(2))
    turtle.left(180)
    square(a / 4, "orange")

    turtle.setposition(x + a / 4 * math.sqrt(2), y + (-(a / 4) * math.sqrt(2)))
    triangle(a / 2, "cyan")

    turtle.setposition(x + a / 4 * math.sqrt(2) * 3/4, y + (-(a / 4) * math.sqrt(2)))
    turtle.right(180)
    triangle(3/4 * (a / 2), "violet")

    turtle.setposition(x + 0, y + 0)
    turtle.right(90)
    parallelogram(a / 4 * math.sqrt(2) * 3/4, a / 4 * math.sqrt(2), "lime")

    turtle.setposition(x + (-(a * 65/1000) * math.sqrt(2)), y + (-(a / 4) * math.sqrt(2)))
    triangle((a / 2) * 3/4, "orchid")

#Person by the left from the square on preview
def figure3(x, y, a):
    
    turtle.up()
    turtle.setposition(x + 0, y + 0)
    turtle.left(45)
    triangle(a, "red")

    turtle.setposition(x + 1/4 * a/2 * math.sqrt(2), y + a/2 * math.sqrt(2))
    turtle.left(90)
    square(a/4, "orange")
    
    turtle.setposition(x + 0, y + a/2 * math.sqrt(2))
    turtle.left(90)
    parallelogram(a/4 * math.sqrt(2), a/2, "lime")

    turtle.setposition(x + 1/4 * a/2 * math.sqrt(2), y + 1/4 * a/2 * math.sqrt(2))
    triangle(a, "yellow")

    turtle.setposition(x + 1/4 * a/2 * math.sqrt(2), y + (-1/2 * a/2 * math.sqrt(2)))
    turtle.left(45)
    triangle(a/2, "cyan")

    turtle.setposition(x + 1/4 * a/2 * math.sqrt(2), y + (-1/2 * a/2 * math.sqrt(2) - 9/10 * a/2 * math.sqrt(2)))
    turtle.left(180)
    triangle(a/4, "violet")

    turtle.setposition(x + (9/10 * (-3/4 * a/2 * math.sqrt(2) - a/4 * math.sqrt(2)/2)), y + (9/10 * (-3/4 * a/2 * math.sqrt(2) - a/4 * math.sqrt(2)/2)))
    turtle.right(45)
    triangle(a/4, "orchid")

#ship
def figure4(x, y, a):

    turtle.up()
    turtle.setposition(x + 0, y + a)
    turtle.right(90)
    triangle(a, "red")

    turtle.setposition(x + a/2, y + a/2)
    turtle.left(45)
    square(a/4 * math.sqrt(2), "orange")

    turtle.setposition(x + 0, y + 0)
    turtle.left(45)
    triangle(a/2, "orchid")

    turtle.setposition(x + a/4 * math.sqrt(2), y + a)
    turtle.left(135)
    triangle(a/2, "violet")

    turtle.setposition(x + a/2, y + 0)
    turtle.left(45)
    triangle(3/4 * a, "cyan")

    turtle.setposition(x + 0, y + (a * 1/10 + a * math.sqrt(2)/2))
    turtle.left(45)
    triangle(a, "yellow")

    turtle.setposition(x + -5/8 * a, y + 0)
    turtle.left(90)
    parallelogram(a/2 * 3/4, 3/4 * a * math.sqrt(2)/2, "lime")

#helicopter
def figure5(x, y, a):

    turtle.up()
    turtle.setposition(x + a/2, y + (-a/2))
    turtle.left(90)
    triangle(a, "yellow")

    turtle.setposition(x + a/2, y + a/2)
    turtle.left(180)
    triangle(a, "red")

    turtle.setposition(x + (-a/4), y + a/2)
    turtle.left(90)
    triangle(3/4 * a, "cyan")

    turtle.setposition(x + a/2, y + a/2)
    parallelogram(a/4 * math.sqrt(2), a/2, "lime")

    turtle.setposition(x + (-a/4), y + (-a/4))
    triangle(a/2, "orchid")

    turtle.setposition(x + 0, y + 0)
    turtle.left(180)
    triangle(a/2, "violet")

    turtle.setposition(x + (-a/2), y + 0)
    turtle.left(45)
    turtle.forward(a/8)
    turtle.right(90)
    square(a/4, "orange")

#Rocket
def figure6(x, y, a):

    turtle.up()
    turtle.setposition(x + 0, y + (-a/2))
    turtle.right(135)
    square(a/4 * math.sqrt(2), "orange")

    turtle.setposition(x + (-a/2), y + (-a/2))
    turtle.left(45)
    triangle(a/2, "violet")

    turtle.setposition(x + a/4, y + (-3/4 * a))
    turtle.left(180)
    triangle(a, "red")

    turtle.right(135)
    turtle.forward(a/4 * math.sqrt(2))
    turtle.left(135)
    parallelogram(a/4 * math.sqrt(2), a/2, "lime")

    turtle.setposition(x + (-a/4), y + 3/4 * a)
    turtle.right(180)
    triangle(a, "yellow")

    turtle.left(45)
    triangle(a/2 * math.sqrt(2), "cyan")

    turtle.left(45)
    triangle(a/2, "orchid")

#Hare
def figure7(x, y, a):

    turtle.up()
    turtle.setposition(x + 0, y + 1/2 * a * math.sqrt(2))
    turtle.right(135)
    triangle(a, "red")

    turtle.setposition(x + (-1/2 * a * math.sqrt(2)), y + (-1/2 * a * math.sqrt(2)))
    turtle.right(180)
    triangle(a, "yellow")

    turtle.setposition(x + (-1/8 * a * math.sqrt(2)), y + (-1/8 * a * math.sqrt(2)))
    turtle.left(180)
    triangle(3/4 * a, "cyan")

    turtle.setposition(x + 1/16 * a * math.sqrt(2), y + (-1/2 * a * math.sqrt(2)))
    turtle.right(90)
    triangle(3/8 * a, "violet")

    turtle.setposition(x + 0, y + (1/8 * a * math.sqrt(2)))
    turtle.left(135)
    triangle(3/8 * a, "orchid")

    turtle.setposition(x + 0, y + 3/8 * a * math.sqrt(2))
    turtle.right(180)
    square(1/4 * a * math.sqrt(2), "orange")

    turtle.setposition(x + 1/8 * a * math.sqrt(2), y + 5/8 * a * math.sqrt(2))
    turtle.left(45)
    parallelogram(1/4 * a * math.sqrt(2), 1/2 * a, "lime")

#Flying Bird
def figure8(x, y, a):

    turtle.up()
    turtle.setposition(x + (-4/9 * a * math.sqrt(2)/2), y + 0)
    turtle.left(45)
    square(a * 4/9, "orange")

    turtle.left(90)
    parallelogram(1/4 * a * math.sqrt(2), 1/2 * a, "lime")
    
    turtle.setposition(x + (-4/9 * a * math.sqrt(2)/2 - 1/4 * a * math.sqrt(2)), y + -1/4 * a * math.sqrt(2))
    turtle.right(90)
    triangle(1/2 * a, "violet")

    turtle.setposition(x + (-4/9 * a * math.sqrt(2)/2 - 1/4 * a * math.sqrt(2)), y + 0)
    turtle.left(180)
    triangle(1/2 * a, "orchid")

    turtle.setposition(x + 4/9 * a * math.sqrt(2)/2, y + 0)
    turtle.right(135)
    turtle.forward(1/2 * a * math.sqrt(2))
    turtle.left(90)
    turtle.forward(1/2 * a * math.sqrt(2))
    turtle.left(135)
    triangle(a, "red")

    turtle.forward(a)
    turtle.right(90)
    triangle(a, "yellow")

    turtle.setposition(x + 4/9 * a * math.sqrt(2)/2, y + 1/4 * a * math.sqrt(2))
    turtle.left(45)
    triangle(1/2 * a * math.sqrt(2), "cyan")

 #Flamingo
def figure9(x, y, a):
    
    turtle.up()
    turtle.setposition(x + 0, y + (-1/2 * a * math.sqrt(2)))
    turtle.left(45)
    triangle(a, "yellow")

    turtle.setposition(x + (-1/2 * a * math.sqrt(2)), y + 1/4 * a * math.sqrt(2))
    turtle.right(90)
    triangle(a, "red")

    turtle.left(45)
    triangle(1/2 * a * math.sqrt(2), "cyan")

    turtle.right(90)
    parallelogram(1/3 * a, 1/3 * a * math.sqrt(2), "lime")

    turtle.setposition(x + 3/8 * a * math.sqrt(2), y + (-1/2 * a * math.sqrt(2)))
    turtle.left(180)
    triangle(3/8 * a * math.sqrt(2), "orchid")

    turtle.setposition(x + 1/2 * a * math.sqrt(2), y + 0)
    turtle.left(90)
    square(9/40 * a * math.sqrt(2), "orange")

    turtle.forward(9/40 * a * math.sqrt(2))
    turtle.right(90)
    turtle.forward(9/40 * a * math.sqrt(2))
    turtle.right(90)
    triangle(9/40 * a * math.sqrt(2) + 9/120 * a * math.sqrt(2), "violet")

turtle.speed("fast")


#figure1(-200, 200, 200)
#figure2(200, 200, 200)
#figure3(0, 0, 200)
#figure4(0, 0, 200)
#figure5(0, 0, 200)
#figure6(0, 0, 200)
#figure7(0, 0, 200)
#figure8(0, 0, 200)
figure9(-200, 200, 200)

turtle.exitonclick()