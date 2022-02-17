"""This program is going to create a scenic night in the mountains."""

__author__ = "730307805"

from random import randint
from turtle import Turtle, colormode, done


# I want to make a mountanous scene with the moon and mini starts in the background.
def main() -> None:
    """The entry point of my scene!"""
    i: int = 0
    shelly: Turtle = Turtle()
    set_background(shelly, 54, 70, 100)
    draw_moon(shelly, 100, 150)

    x: float = -500
    y: float = -350
    while (i < 7):
        draw_mountains(shelly, x, y)
        x += 200
        i += 1

    c: int = 0
    while (c < 15):
        one: float = randint(-500, 500)
        two: float = randint(100, 200)
        draw_stars(shelly, one, two)
        c += 1

    done()


def draw_mountains(shelly: Turtle, x: float, y: float) -> None:
    """Draw a triangle of the given size whose top corner is located at x, y."""
    # change color to be more realistic for mountains at night
    shelly.hideturtle()
    colormode(255)
    shelly.color(118.0, 132.0, 158.0)
    shelly.penup()
    shelly.goto(x, y)
    shelly.pendown()
    shelly.begin_fill()

    i: int = 0
    while(i < 3):
        shelly.forward(300)
        shelly.right(120)
        i += 1

    shelly.end_fill()


def draw_moon(shelly: Turtle, x: float, y: float) -> None:
    """Draw a circle meant to be the moon."""
    shelly.ht()
    shelly.color(228, 228, 204)
    shelly.penup()
    shelly.goto(x, y)
    shelly.pendown()
    shelly.begin_fill()

    i: int = 0
    while i <= 2:
        shelly.circle(120, 180)
        i += 1
    
    shelly.end_fill()


def set_background(shelly: Turtle, r: float, g: float, b: float) -> None:
    """This function sets the background color, yeah."""
    shelly.ht()
    colormode(255)
    shelly.screen.bgcolor(r, g, b)


def draw_stars(shelly: Turtle, x: float, y: float) -> None:
    """This function draws stars in the night sky."""
    shelly.ht()
    shelly.penup()
    shelly.goto(x, y)
    shelly.pendown()
    shelly.begin_fill()
    shelly.color("white")
    i: int = 0
    while(i < 5):
        shelly.forward(50)
        shelly.left(145)
        i += 1
    shelly.end_fill()


if __name__ == "__main__":
    main()

# I've attempted to "something fun" by randomizing the coordinates that the stars are drawn at.