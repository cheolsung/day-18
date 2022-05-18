from turtle import Turtle, Screen
from random import randint

my_screen = Screen()
my_screen.colormode(255)
ching = Turtle()
ching.hideturtle()
ching.speed(0)
print(ching.pensize(10))

for _ in range(500):
    ching.color(randint(0,255),randint(0,255),randint(0,255))
    angle = randint(0,3)*90
    ching.forward(20)
    ching.right(angle)

my_screen.screensize(800,800)
my_screen.exitonclick()
