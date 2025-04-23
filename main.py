import time

import sys
sys.path.append("game-objects")
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
placar = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()

    #Bouncing for y coordinate
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Boucing in the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Check the score in case a paddle
    if ball.xcor() > 350:
        placar.writeScoreLeft()
        ball.reset_position()
    elif ball.xcor() < -350:
        placar.writeScoreRight()
        ball.reset_position()



    ball.move()
    time.sleep(ball.move_speed)



screen.exitonclick()