import turtle
import random
from turtle import Turtle
import time
turtle.colormode(255)

SPEED = 3
INCREMENT_SPEED = 10


class Cars:
    def __init__(self):
        self.carList = []
        self.color_list = ["red", "green", "blue", "orange", "yellow"]
        self.speed = SPEED

    def create_cars(self):
        random_count = random.randint(1, 6)
        if random_count == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(280, car.ycor() + random.randrange(-280, 280))
            car.color(random.choice(self.color_list))
            self.carList.append(car)

    def move_cars(self):
        for car in self.carList:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += INCREMENT_SPEED






