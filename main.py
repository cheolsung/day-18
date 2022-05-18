from turtle import Turtle, Screen
from random import randint

my_screen = Screen()
my_screen.colormode(255)
ching = Turtle()
ching.hideturtle()
ching.speed(0)
print(ching.pensize(1))

number_of_circles = 100
for i in range(number_of_circles):
    ching.color(randint(0,255),randint(0,255),randint(0,255))
    angle = 365/number_of_circles
    ching.circle(100)
    ching.seth(angle*(i+1))

my_screen.screensize(800,800)
my_screen.exitonclick()
