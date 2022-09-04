from ball import Ball
from  turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Arial",80,"normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    def update_score_l(self):
        self.l_score+=1
        self.update_Scoreboard()


    def update_score_r(self):
        self.r_score+=1
        self.update_Scoreboard()
