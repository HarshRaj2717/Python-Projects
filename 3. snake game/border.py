from turtle import Turtle
import snake
import gameover


def create_border():
    border1 = Turtle()
    border1.hideturtle()
    border1.penup()
    border1.goto(280, 280)
    border1.pendown()
    border1.color("red")
    border1.pensize(10)
    border1.speed(0)
    for i in range(4):
        border1.right(90)
        border1.forward(560)


def border_collision():
    if snake.all_turtles[0].xcor() > 260 or snake.all_turtles[0].ycor() > 260:
        snake.game_on = False
        gameover.reason = "Collided with wall"
        gameover.game_over()
    elif snake.all_turtles[0].xcor() < -260 or snake.all_turtles[0].ycor() < -260:
        snake.game_on = False
        gameover.reason = "Collided with wall"
        gameover.game_over()
