from turtle import Turtle, Screen
import scores

reason = None


def game_over():
    global reason
    screen1 = Screen()
    screen1.clear()
    screen1.bgcolor("Black")
    over = Turtle()
    over.hideturtle()
    over.color("white")
    s = f'''Game Over
({reason})
==========
Final Score : {scores.current_score}'''
    over.write(s, False, "center", ("Arial", 40, 'normal'))
    over.color("dark gray")
    s = "Click anywhere to exit."
    over.penup()
    over.sety(-100)
    over.write(s, False, "center", ("Arial", 20, 'normal'))
