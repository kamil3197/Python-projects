from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake.py Game")
screen.tracer(0)

#class objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# snake operating by keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect colision with wall
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        scoreboard.game_over()

    #detect colision with tail
    for segment in snake.start_snake[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()