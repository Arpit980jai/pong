from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.go_up()
        self.go_dowm()

    def go_up(self):
        num_y = self.ycor() + 20
        self.goto(self.xcor(), num_y)

    def go_dowm(self):
        num_y = self.ycor() - 20
        self.goto(self.xcor(), num_y)