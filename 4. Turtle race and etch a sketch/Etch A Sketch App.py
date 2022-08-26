from turtle import Turtle, Screen

screen1 = Screen()
turtle1 = Turtle()
turtle1.speed(0)


def w():
    turtle1.forward(20)


def s():
    turtle1.backward(20)


def a():
    turtle1.left(10)


def d():
    turtle1.right(10)


def c():
    turtle1.clear()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()


screen1.onkey(w, 'w')
screen1.onkey(s, 's')
screen1.onkey(a, 'a')
screen1.onkey(d, 'd')
screen1.onkey(c, 'c')
screen1.listen()
screen1.mainloop()
