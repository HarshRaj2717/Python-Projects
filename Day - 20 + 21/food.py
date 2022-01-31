from turtle import Turtle
import random
import snake
import scores

food1 = Turtle("circle")
food1.speed(0)


def create_food():
    global food1
    food1.shapesize(0.5, 0.5)
    food1.color("yellow")
    food1.penup()
    food1.goto(random.randint(-260, 260), random.randint(-260, 260))


def food_collision():
    global food1
    if food1.distance(snake.all_turtles[0]) < 15:
        create_food()
        scores.current_score += 1
        scores.write_score()
        snake.increase_size()

