from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("midnightblue")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0), "teal")
l_paddle = Paddle((-350, 0), "cadetblue")
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.06)
    screen.update()
    ball.move()

    #detect the collision in the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect the collision in the paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()