from turtle import Turtle, Screen

screen1 = Screen()
all_turtles = []


def starting_turtles():
    global all_turtles, screen1
    x = 0
    for i in range(5):
        turtle1 = Turtle("square")
        all_turtles.append(turtle1)
        turtle1.color("white")
        turtle1.speed(2)
        turtle1.penup()
        turtle1.setx(x)
        x -= 20


def go_fd():
    global all_turtles, screen1
    l1 = all_turtles.copy()
    l1.reverse()
    game_on = True
    while game_on:
        for i in range(len(l1)-1):
            x = l1[i+1].xcor()
            y = l1[i+1].ycor()
            l1[i].goto(x, y)
        l1[-1].forward(10)


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
