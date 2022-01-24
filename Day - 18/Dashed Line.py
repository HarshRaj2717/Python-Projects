from turtle import Turtle, Screen

screen1 = Screen()
screen1.bgcolor("black")

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.color("white", "red")

turtle1.penup()
turtle1.backward(500)
turtle1.pendown()

for i in range(50):
    turtle1.forward(10)
    turtle1.penup()
    turtle1.forward(10)
    turtle1.pendown()

screen1.mainloop()
