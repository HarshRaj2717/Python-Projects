from turtle import Turtle
import random

all_turtles = []
game_on = True


def starting_turtles():
    global all_turtles
    x = 0
    for i in range(5):
        turtle1 = Turtle("square")
        all_turtles.append(turtle1)
        turtle1.color(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245))
        turtle1.speed(0)
        turtle1.penup()
        turtle1.setx(x)
        x -= 20


def increase_size():
    global all_turtles
    x = all_turtles[-1].xcor()
    y = all_turtles[-1].ycor()
    for i in range(1):
        turtle1 = Turtle("square")
        turtle1.hideturtle()
        all_turtles.append(turtle1)
        turtle1.color(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245))
        turtle1.speed(0)
        turtle1.penup()
        turtle1.setx(x)
        turtle1.sety(y)
        turtle1.showturtle()
        x -= 20
        y -= 20


def go_fd():
    global all_turtles
    l1 = all_turtles.copy()
    l1.reverse()
    for i in range(len(l1)-1):
        x = l1[i+1].xcor()
        y = l1[i+1].ycor()
        l1[i].goto(x, y)
    l1[-1].forward(20)


def go_up():
    global all_turtles
    if all_turtles[0].heading() == 0:
        all_turtles[0].left(90)

    elif all_turtles[0].heading() == 180:
        all_turtles[0].right(90)


def go_down():
    global all_turtles
    if all_turtles[0].heading() == 0:
        all_turtles[0].right(90)

    elif all_turtles[0].heading() == 180:
        all_turtles[0].left(90)


def go_left():
    global all_turtles
    if all_turtles[0].heading() == 90:
        all_turtles[0].left(90)

    elif all_turtles[0].heading() == 270:
        all_turtles[0].right(90)


def go_right():
    global all_turtles
    if all_turtles[0].heading() == 90:
        all_turtles[0].right(90)

    elif all_turtles[0].heading() == 270:
        all_turtles[0].left(90)
