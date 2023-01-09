from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_on = True
while game_on: 
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() <-290:
        ball.y_bounce()

    #Detect collision with paddle on the right
    if ball.distance(right_paddle) < 50 and ball.xcor()>320 or ball.distance(left_paddle) < 50 and ball.xcor() <-320:
        ball.x_bounce()
    
    #Detect Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_goal()
    
    #Detect Left paddle miss
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.right_goal()



screen.exitonclick()


