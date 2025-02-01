from turtle import Screen
import pong_physics
import ball_physics
import time
import scoreboard

screen = Screen()
screen.screensize(500, 500)
screen.tracer(0)
screen.bgcolor("black")

scores = scoreboard.Scoreboard()

screen.update()

l_paddle = pong_physics.Pong(-315)
r_paddle = pong_physics.Pong(310)

screen.listen()
screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)

ball = ball_physics.Ball()
neg = -1

game_is_on = True
while game_is_on:
    screen.update()
    ball.start()
    time.sleep(ball.speed_pos)
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if (ball.xcor() > 300 and ball.xcor() < 320 and 
    ball.ycor() < r_paddle.ycor() + 50 and 
    ball.ycor() > r_paddle.ycor() - 50):
        ball.bounce_x()
    
    # Left paddle collision    
    if (ball.xcor() < -300 and ball.xcor() > -320 and 
    ball.ycor() < l_paddle.ycor() + 50 and 
    ball.ycor() > l_paddle.ycor() - 50):
        ball.bounce_x()

    if ball.xcor() > 330:
        ball.reset_position()
        scores.score_r()

    if ball.xcor() < -330:
        ball.reset_position()
        scores.score_l()

    if scores.l_score == 10 or scores.r_score == 10:
        game_is_on = False


screen.exitonclick()
