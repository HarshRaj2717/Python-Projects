from turtle import Turtle, Screen
import snake


def main():
    screen1 = Screen()
    screen1.setup(width=800, height=600)
    screen1.bgcolor("black")
    screen1.title("Snaky Snaky")
    screen1.colormode(255)

    snake.starting_turtles()

    screen1.listen()
    screen1.onkey(snake.go_up, "Up")
    screen1.onkey(snake.go_down, "Down")
    screen1.onkey(snake.go_left, "Left")
    screen1.onkey(snake.go_right, "Right")

    game_on = True
    while game_on:
        snake.go_fd()

    screen1.mainloop()


if __name__ == "__main__":
    main()
