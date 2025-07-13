from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, POSSITION):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(POSSITION)
        self.shapesize(5, 1)

    def go_up(self):
        if self.ycor() < 235:
            self.goto(self.xcor(), self.ycor() + 40)

    def go_down(self):
        if self.ycor() > -235:
            self.goto(self.xcor(), self.ycor() - 40)