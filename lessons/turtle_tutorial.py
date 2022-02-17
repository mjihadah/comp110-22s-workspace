"""Learning how to use the turtle graphics."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)

colormode(255)
leo.color(255, 219, 51)
leo.penup()
leo.goto(-150, -100)
leo.pendown()
leo.begin_fill()

i: int = 0
while(i < 5):
    leo.forward(50)
    leo.left(145)
    i += 1

leo.end_fill()

colormode(255)
leo.color(255, 219, 51)
leo.penup()
leo.goto(-150, -100)
leo.pendown()
leo.begin_fill()

i: int = 0
while i <= 2:
    leo.circle(120, 180)
    i += 1



done()
