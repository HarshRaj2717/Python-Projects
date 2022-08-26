import random
from turtle import Turtle, Screen

screen1 = Screen()
screen1.colormode(255)

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.speed(0)
turtle1.pensize(20)

for i in range(200):
    turtle1.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    turtle1.forward(50)
    turtle1.right(random.choice([0, 90, 180, 270]))

screen1.mainloop()
