from turtle import Turtle, Screen

screen1 = Screen()
screen1.bgcolor("black")

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.penup()
turtle1.goto(-50, 50)
turtle1.pendown()
turtle1.color("white", "red")
for i in range(4):
    turtle1.forward(100)
    turtle1.right(90)

screen1.mainloop()
