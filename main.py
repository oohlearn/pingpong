from turtle import Turtle, Screen
import time
from player import Player
from score import ScoreBoard
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)


player_right = Player()
player_left = Player()
score = ScoreBoard()
ball = Ball()
game_is_on = True

player_left.goto(-350, 0)
player_right.goto(350, 0)

screen.listen()
screen.onkeypress(player_right.move_up, "Up")
screen.onkeypress(player_right.move_down, "Down")
screen.onkeypress(player_left.move_up, "w")
screen.onkeypress(player_left.move_down, "s")


while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_right) < 50 and ball.xcor() > 320 or ball.distance(player_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.miss()
        score.get_score("left")

    if ball.xcor() < -350:
        ball.miss()
        score.get_score("right")



screen.exitonclick()
