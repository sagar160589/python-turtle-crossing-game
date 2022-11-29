from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_score = 0
        self.penup()
        self.goto(-280, 280)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.write(f"Current Score: {self.initial_score}", font=('Arial', 8, 'bold'))

    def increase_score(self):
        self.clear()
        self.initial_score += 1
        self.write(f"Current Score: {self.initial_score}", font=('Arial', 8, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! your final Score is: {self.initial_score}", align='center', font=('Arial', 8, 'bold'))


