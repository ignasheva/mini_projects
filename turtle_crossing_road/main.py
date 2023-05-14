import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_new_car()
    car.move_cars()
    #Detect collision with a car
    for each_car in car.all_cars:
        if player.distance(each_car) < 25:
            game_is_on = False
            level.game_over()
    #Detect the player has reached the top edge of the screen
    if player.ycor() > 280:
        player.starting_position()
        level.level_up()
        car.increase_speed()

screen.exitonclick()
