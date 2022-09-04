from turtle import Screen,Turtle
from paddle import Paddle
from  ball import  Ball
import time
from scoreboard import Score
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)



r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))
ball=Ball()

scoreboard=Score()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_dowm,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_dowm,"s")



game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect Colision with wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()
    #Detect the collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        print ("make COntact")
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.update_score_l()

    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.update_score_r()


















screen.exitonclick()