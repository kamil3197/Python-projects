from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


game_on = True

screen = Screen()
screen.setup(800,600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detect collision with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

#detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
# restart game after point

    #R_PADDLE
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #L_PADDLE
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()