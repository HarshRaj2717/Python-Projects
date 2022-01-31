import snake
import gameover


def tail_collision():
    n = 0
    for i in snake.all_turtles:
        n += 1
        if n > 2 and i.distance(snake.all_turtles[0]) < 10:
            snake.game_on = False
            gameover.reason = "Collided with tail"
            gameover.game_over()
