# Drawing a triangle, quare, pentagon, hexagon, heptagon, octagon, nonagon, decagon with randomised colors.

import random
from turtle import Turtle, Screen

screen1 = Screen()
screen1.bgcolor("black")
screen1.colormode(255)

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.speed(0)
turtle1.pensize(2)

turtle1.penup()
turtle1.setx(-50)
turtle1.sety(300)
turtle1.pendown()

# Use the following commented statements to make infinite shapes.
# sides = 2

# while True:
for sides in range(3, 11):
    # sides += 1
    angle = 180 - (360 / sides)
    turtle1.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    for i in range(sides):
        turtle1.forward(100)
        turtle1.right(180 - angle)

screen1.mainloop()
