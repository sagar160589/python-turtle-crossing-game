from turtle import Screen
from turtlecar import TurtleCar
from cars import Cars
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing game")
is_game_on = True
screen.tracer(0)

turtle_car = TurtleCar((0, -280))
car = Cars()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=turtle_car.move_up, key="Up")

while is_game_on:
    screen.update()
    car.create_cars()
    car.move_cars()
    time.sleep(0.5)

    # turtle_car.detect_collison(car.carList)
    for cars in car.carList:
        if cars.distance(turtle_car) < 20:
            is_game_on = False
            scoreboard.game_over()

    # detect end of wall upward
    if turtle_car.ycor() > 300:
        turtle_car.reset()
        car.increase_speed()
        scoreboard.increase_score()


screen.exitonclick()