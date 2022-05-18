from turtle import Turtle, Screen
from random import randint
import math


my_screen = Screen()
my_screen.colormode(255)
ching = Turtle()
ching.hideturtle()
ching.speed(0)
print(ching.pensize(1))

number_of_circles = 50
radius = 100
for i in range(number_of_circles):
    ching.color(randint(0,255),randint(0,255),randint(0,255))
    angle = 2*math.pi/number_of_circles
    ching.penup()
    ching.goto(radius*math.cos(angle*i),radius*math.sin(angle*i))
    ching.pendown()
    ching.circle(150)

my_screen.screensize(800,800)
my_screen.exitonclick()
