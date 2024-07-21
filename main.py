from turtle import Screen
from ball import Ball
from paddle import Paddle
from brick import make_wall, bricks_hit
from score import Score
from time import sleep

screen = Screen()
screen.title('BREAKOUT')
screen.bgcolor('black')
screen.setup(width=1200, height=600)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
current_score = Score()

screen.onkeypress(fun=paddle.move_left, key='Left')
screen.onkeypress(fun=paddle.move_right, key='Right')
screen.listen()

game_is_on = True
make_wall()
while game_is_on:
    ball.move(paddle=paddle)
    if len(bricks_hit) > current_score.score:
        current_score.score += 1
        current_score.update_score()
        if current_score.score == 180:
            game_is_on = False
    if ball.ycor() <= -290:
        game_is_on = current_score.game_over()
        sleep(0.5)
        if game_is_on:
            paddle.initialize()
            ball.initialize()
    screen.update()

screen.exitonclick()
