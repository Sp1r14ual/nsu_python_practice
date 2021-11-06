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
def figure1():
    #Change parameter below to change size
    a = 500
    #Change parameter above to change size

    turtle.up()
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

    turtle.up()
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
    
    turtle.up()
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

    turtle.up()
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

#helicopter
def figure5():
    #Change parameter below to change painting's size
    a = 300
    #Change parameter above to change painting's size

    turtle.up()
    turtle.setposition(a/2, -a/2)
    turtle.left(90)
    triangle(a, "yellow")

    turtle.setposition(a/2, a/2)
    turtle.left(180)
    triangle(a, "red")

    turtle.setposition(-a/4, a/2)
    turtle.left(90)
    triangle(3/4 * a, "cyan")

    turtle.setposition(a/2, a/2)
    parallelogram(a/4 * math.sqrt(2), a/2, "lime")

    turtle.setposition(-a/4, -a/4)
    triangle(a/2, "orchid")

    turtle.setposition(0, 0)
    turtle.left(180)
    triangle(a/2, "violet")

    turtle.setposition(-a/2, 0)
    turtle.left(45)
    turtle.forward(a/8)
    turtle.right(90)
    square(a/4, "orange")

#Rocket
def figure6():
    #Change parameter below to change painting's size
    a = 300
    #Change parameter above to change painting's size

    turtle.up()
    turtle.setposition(0, -a/2)
    turtle.right(135)
    square(a/4 * math.sqrt(2), "orange")

    turtle.setposition(-a/2, -a/2)
    turtle.left(45)
    triangle(a/2, "violet")

    turtle.setposition(a/4, -3/4 * a)
    turtle.left(180)
    triangle(a, "red")

    turtle.right(135)
    turtle.forward(a/4 * math.sqrt(2))
    turtle.left(135)
    parallelogram(a/4 * math.sqrt(2), a/2, "lime")

    turtle.setposition(-a/4, 3/4 * a)
    turtle.right(180)
    triangle(a, "yellow")

    turtle.left(45)
    triangle(a/2 * math.sqrt(2), "cyan")

    turtle.left(45)
    triangle(a/2, "orchid")

#Hare
def figure7():
    #Change parameter below to change painting's size
    a = 300
    #Change parameter above to change painting's size

    turtle.up()
    turtle.setposition(0, 1/2 * a * math.sqrt(2))
    turtle.right(135)
    triangle(a, "red")

    turtle.setposition(-1/2 * a * math.sqrt(2), -1/2 * a * math.sqrt(2))
    turtle.right(180)
    triangle(a, "yellow")

    turtle.setposition(-1/8 * a * math.sqrt(2), -1/8 * a * math.sqrt(2))
    turtle.left(180)
    triangle(3/4 * a, "cyan")

    turtle.setposition(1/16 * a * math.sqrt(2), -1/2 * a * math.sqrt(2))
    turtle.right(90)
    triangle(3/8 * a, "violet")

    turtle.setposition(0, 1/8 * a * math.sqrt(2))
    turtle.left(135)
    triangle(3/8 * a, "orchid")

    turtle.setposition(0, 3/8 * a * math.sqrt(2))
    turtle.right(180)
    square(1/4 * a * math.sqrt(2), "orange")

    turtle.setposition(1/8 * a * math.sqrt(2), 5/8 * a * math.sqrt(2))
    turtle.left(45)
    parallelogram(1/4 * a * math.sqrt(2), 1/2 * a, "lime")

#Flying Bird
def figure8():
    #Change parameter below to change painting's size
    a = 400
    #Change parameter above to change painting's size

    turtle.up()
    turtle.setposition(-4/9 * a * math.sqrt(2)/2, 0)
    turtle.left(45)
    square(a * 4/9, "orange")

    turtle.left(90)
    parallelogram(1/4 * a * math.sqrt(2), 1/2 * a, "lime")
    
    turtle.setposition(-4/9 * a * math.sqrt(2)/2 - 1/4 * a * math.sqrt(2), -1/4 * a * math.sqrt(2))
    turtle.right(90)
    triangle(1/2 * a, "violet")

    turtle.setposition(-4/9 * a * math.sqrt(2)/2 - 1/4 * a * math.sqrt(2), 0)
    turtle.left(180)
    triangle(1/2 * a, "orchid")

    turtle.setposition(4/9 * a * math.sqrt(2)/2, 0)
    turtle.right(135)
    turtle.forward(1/2 * a * math.sqrt(2))
    turtle.left(90)
    turtle.forward(1/2 * a * math.sqrt(2))
    turtle.left(135)
    triangle(a, "red")

    turtle.forward(a)
    turtle.right(90)
    triangle(a, "yellow")

    turtle.setposition(4/9 * a * math.sqrt(2)/2, 1/4 * a * math.sqrt(2))
    turtle.left(45)
    triangle(1/2 * a * math.sqrt(2), "cyan")

 #Flamingo
def figure9():
    
    turtle.up()
    turtle.setposition(0, -100 * math.sqrt(2))
    turtle.left(45)
    triangle(200, "yellow")

    turtle.setposition(-100 * math.sqrt(2), 1/2 * 100 * math.sqrt(2))
    turtle.right(90)
    triangle(200, "red")

    turtle.left(45)
    triangle(100 * math.sqrt(2), "cyan")

    turtle.right(90)
    parallelogram(1/3 * 200, 2/3 * 100 * math.sqrt(2), "lime")

    turtle.setposition(75 * math.sqrt(2), -100 * math.sqrt(2))
    turtle.left(180)
    triangle(75 * math.sqrt(2), "orchid")

    turtle.setposition(100 * math.sqrt(2), 0)
    turtle.left(90)
    square(9/10 * 1/2 * 100 * math.sqrt(2), "orange")

    turtle.forward(9/10 * 1/2 * 100 * math.sqrt(2))
    turtle.right(90)
    turtle.forward(9/10 * 1/2 * 100 * math.sqrt(2))
    turtle.right(90)
    triangle(9/10 * 1/2 * 100 * math.sqrt(2) + 1/3 * 9/10 * 1/2 * 100 * math.sqrt(2), "violet")














'''
print("Hello! What picture would you like to be presented?")
print("Type the number:")
print("Complicated square: 1")
print("Person: 2")
print("Another person: 3")
print("Ship: 4")
print("Helicopter: 5")
print("Rocket: 6")
print("Hare: 7")
print("Flying Bird: 8")
print("Flamingo: 9")

user_choice = input()
'''
turtle.speed("fast")
'''
if user_choice == "1":
    figure1()
elif user_choice == "2":
    figure2()
elif user_choice == "3":
    figure3()
elif user_choice == "4":
    figure4()
elif user_choice == "5":
    figure5()
elif user_choice == "6":
    figure6()
elif user_choice == "7":
    figure7()
elif user_choice == "8":
    figure8()
elif user_choice == "9":
    figure9()
else:
    print("Error! There is no such option.")
'''
figure9()
turtle.exitonclick()