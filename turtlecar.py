from turtle import Turtle


class TurtleCar(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(position)
        self.y_move = 10

    def move_up(self):
        self.goto(0, self.ycor() + self.y_move)

    def reset(self):
        self.penup()
        self.setheading(90)
        self.goto(0, -280)


