from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()


def set_shape_and_color(turtle):
    turtle.shape("turtle")
    turtle.color("red")


def set_position(turtle):
    print(turtle.position())
    turtle.up()
    turtle.sety(-300)
    turtle.down()


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


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_polygon(sides):
    """draws a polygon with n sides and random colors"""
    angle = 360 / sides
    #
    #   set color mode!!!
    #
    screen.colormode(255)
    tim.color(random_color())
    for _ in range(sides):
        tim.forward(100)
        tim.left(angle)


def draw_polygons(number_of_polygons):
    for _ in range(3, number_of_polygons):
        draw_polygon(_)


def draw_circle(radius, heading, *color):
    tim.setheading(heading)
    screen.colormode(255)
    tim.color(*color)
    tim.circle(radius)


def draw_spyrograph(gap):
    tim.speed(0)
    for _ in range(1, 360, gap):
        draw_circle(100, _, *random_color())


draw_spyrograph(5)

screen.exitonclick()
