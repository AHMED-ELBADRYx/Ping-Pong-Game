from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.updete_scoreboard()

    def l_point(self):
        self.left_score += 1
        self.updete_scoreboard()

    def r_point(self):
        self.right_score += 1
        self.updete_scoreboard()

    def updete_scoreboard(self):
        self.clear()
        self.goto(-250, 160)
        self.write(self.left_score, align = "center", font = ("courier", 20, "bold"))
        self.goto(250, 160)
        self.write(self.right_score, align = "center", font = ("courier", 20, "bold"))