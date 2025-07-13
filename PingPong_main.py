from turtle import Turtle, Screen
import turtle  # For the exception handling
import tkinter # For the exception handling
from PingPong_paddle import Paddle
from PingPong_ball import Ball
from PingPong_score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PingPong Game")
screen.tracer(0)
 
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score = Scoreboard()

default_sleep = 0.1
game_on = True
try:
    while game_on:
        screen.listen()
        screen.onkey(r_paddle.go_up, "Up")
        screen.onkey(r_paddle.go_down, "Down")
        screen.onkey(l_paddle.go_up, "w")
        screen.onkey(l_paddle.go_down, "s")
        screen.update()
        time.sleep(default_sleep)
        ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

        if (ball.ycor() >= 290) or (ball.ycor() <= -290):
            ball.y_move *= -1

        if (ball.xcor() >= 350 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= - 350 and ball.distance(l_paddle) <= 50):
            ball.x_move *= -1
            default_sleep *= 0.9

        if ball.xcor() > 390:
            ball.hideturtle()
            ball.goto(0, 0)
            ball.showturtle()
            ball.x_move *= -1
            default_sleep = 0.1
            score.l_point()

        if ball.xcor() < -390:
            ball.hideturtle()
            ball.goto(0, 0)
            ball.showturtle()
            ball.x_move *= -1
            default_sleep = 0.1
            score.r_point()

        if score.left_score == 5:
            game_on = False
            l_win = Turtle()
            l_win.hideturtle()
            l_win.penup()
            l_win.color("white")
            l_win.write("Left player is win", align="center", font=("courier", 30, "bold"))

        if score.right_score == 5:
            game_on = False
            r_win = Turtle()
            r_win.hideturtle()
            r_win.penup()
            r_win.color("white")
            r_win.write("Right player is win", align="center", font=("courier", 30, "bold"))

    screen.exitonclick()
except (turtle.Terminator, tkinter.TclError):
    pass