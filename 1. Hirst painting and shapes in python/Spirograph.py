import random
from turtle import Turtle, Screen

screen1 = Screen()
screen1.bgcolor("black")
screen1.colormode(255)

turtle1 = Turtle()
turtle1.speed(0)

for tilt_angle in range(0, 360):
    turtle1.right(tilt_angle)
    turtle1.circle(150)
    turtle1.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

screen1.mainloop()
