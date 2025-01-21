from turtle import Screen
import pong_physics
import ball_physics
import time
import scoreboard

screen = Screen()
screen.screensize(500, 500)
screen.tracer(0)
screen.bgcolor("black")

l_paddle = pong_physics.Pong(-315)
r_paddle = pong_physics.Pong(310)
scores = scoreboard.Scoreboard()

screen.update()
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

    if ball.distance(r_paddle) < 50 and ball.xcor() > 308 or ball.distance(l_paddle) < 50 and ball.xcor() < -308:
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
