from turtle import Turtle

current_score = 0

scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.speed(0)
scoreboard.color("dark gray")


def write_score():
    global current_score
    scoreboard.clear()
    s = f"Score : {current_score}"
    scoreboard.write(s, False, "center", ("Arial", 30, 'normal'))
