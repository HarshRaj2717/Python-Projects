from turtle import Turtle, Screen
import colorgram
import random

screen1 = Screen()
screen1.colormode(255)

colors = colorgram.extract("hirst_sample.jpg", 20)
list_of_colors = []
for i in colors:
    list_of_colors.append((i.rgb[0], i.rgb[1], i.rgb[2]))

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.speed(0)

x = -200
y = -300
while y < 200:
    x = -200
    y += 50
    turtle1.penup()
    turtle1.goto(x, y)
    turtle1.pendown()
    while x <= 200:
        turtle1.dot(15, random.choice(list_of_colors))
        turtle1.penup()
        turtle1.forward(50)
        x += 50
        turtle1.pendown()

screen1.mainloop()
