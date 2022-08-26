from turtle import Screen
import time
import food
import scores
import snake
import border
import tail


def main():
    screen1 = Screen()
    screen1.setup(width=600, height=600)
    screen1.bgcolor("black")
    screen1.title("Snaky Snaky")
    screen1.colormode(255)

    border.create_border()
    snake.starting_turtles()
    food.create_food()
    scores.write_score()

    screen1.listen()
    screen1.onkey(snake.go_up, "Up")
    screen1.onkey(snake.go_down, "Down")
    screen1.onkey(snake.go_left, "Left")
    screen1.onkey(snake.go_right, "Right")

    screen1.tracer(0)

    while snake.game_on:
        snake.go_fd()
        border.border_collision()
        food.food_collision()
        tail.tail_collision()
        screen1.update()
        time.sleep(0.1)

    screen1.exitonclick()


if __name__ == "__main__":
    main()
