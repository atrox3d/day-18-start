from turtle import Turtle, Screen
import random


screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.color("red")
print(tim.position())
tim.up()
tim.sety(-300)
tim.down()


def draw_square():
    """draw a sqaure"""
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


def draw_alternate_line():
    tim.left(180)
    for _ in range(10):
        tim.forward(10)
        tim.up()
        tim.forward(10)
        tim.down()


#draw_square()
def draw_polygon(sides):
    angle = 360 / sides
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    screen.colormode(255)
    tim.color(r, g, b)
    for _ in range(sides):
        tim.forward(100)
        tim.left(angle)


for _ in range(3, 15):
    draw_polygon(_)


screen.exitonclick()

