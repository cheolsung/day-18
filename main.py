from turtle import Turtle, Screen
import random

ching = Turtle()
ching.shape("turtle")
colors=["red","blue","magenta","yellow","aquamarine","bisque"]

for sides in range(3,11):
    ching.color(random.choice(colors))
    angle = 360/sides
    for _ in range(sides):
        ching.forward(100)
        ching.right(angle)

my_screen = Screen()
my_screen.screensize(800,800)
my_screen.exitonclick()
