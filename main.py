from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")


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
    print(type(angle))
    for _ in range(sides):
        tim.forward(100)
        tim.left(angle)


for _ in range(3, 11):
    draw_polygon(_)


screen = Screen()
screen.exitonclick()

