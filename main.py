from turtle import Turtle, Screen

ching = Turtle()
ching.shape("turtle")
ching.color("magenta")
for _ in range(10):
    ching.forward(10)
    ching.penup()
    ching.forward(10)
    ching.pendown()

my_screen = Screen()
my_screen.screensize(800,800)
my_screen.exitonclick()
