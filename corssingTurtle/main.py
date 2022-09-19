import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.ride()

    #collision with cars
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            player.reset_position()

    #end road for turtle
    if player.player_at_finish_line():
        player.reset_position()
        cars.next_lvl()
        scoreboard.increase_level()


screen.exitonclick()