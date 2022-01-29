from turtle import Turtle, Screen
import random

is_race_on = False
screen1 = Screen()
screen1.setup(width=500, height=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

user_bet = screen1.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            screen1.clear()
            screen1.bgcolor(winning_color)
            screen1.delay(2)
            screen1.exitonclick()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        turtle.forward(random.randint(0, 10))
