from turtle import Screen
from food import Food
from score import Score
import time
from snake import Snake
import winsound

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_continue = True

while game_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_continue = False
        score.reset()
        score.game_over()
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            game_continue = False
            score.reset()
            score.game_over()
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


screen.exitonclick()

