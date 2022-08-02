from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game = True
i = 0.09
while game:
    time.sleep(i)
    screen.update()
    ball.move()
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()
    if ball.xcor() == r_paddle.xcor() - 20:
        if ball.ycor() in range(r_paddle.ycor() - 50, r_paddle.ycor() + 51):
            ball.reverse()
    if ball.xcor() == l_paddle.xcor() + 20:
        if ball.ycor() in range(l_paddle.ycor() - 50, l_paddle.ycor() + 51):
            ball.reverse()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.restart()

screen.exitonclick()
