from turtle import Turtle, Screen
from random import randint
import math


my_screen = Screen()
my_screen.colormode(255)
ching = Turtle()
ching.hideturtle()
ching.speed(0)
ching.pensize(4)

number_of_circles = 100
size_of_circles=50
radius = 100
ching.penup()
ching.sety(-radius)
for i in range(number_of_circles):
    ching.color(randint(0,255),randint(0,255),randint(0,255))
    ching.penup()
    ching.goto(radius*math.sin(2*math.pi*i/number_of_circles),radius*math.cos(2*math.pi*i/number_of_circles))
    ching.seth(360-360/number_of_circles*i)
    ching.pendown()
    ching.circle(size_of_circles)

my_screen.exitonclick()
