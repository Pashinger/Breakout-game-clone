from turtle import Turtle
from random import randint
from brick import all_bricks
from sounds import Sound
from paddle import Paddle
from typing import Optional


STARTING_POSITION = 0, -230
sound = Sound()
last_side = ['dummy']


def starting_angle() -> int:
    """Randomly set the starting direction of the ball."""
    starting_angle = randint(20, 160)
    while 92 > starting_angle > 88:
        starting_angle = randint(20, 160)
    return starting_angle


class Ball(Turtle):
    """Manage the properties and behaviour of the ball and its collisions with the other objects."""

    speed: float

    def __init__(self) -> None:
        """Initialize a Ball object inheriting from the Turtle class."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('circle')
        self.color('white')
        self.setheading(starting_angle())
        self.showturtle()
        self.speed = 2.4

    def increase_speed(self) -> None:
        """Increase the speed of the ball after a brick is hit."""
        if len(all_bricks) < 60:
            self.speed += 0.002

    def detect_collision(self, x: float, y: float, paddle: Paddle) -> Optional[str]:
        """Encompass functions which check for collisions with the paddle and bricks, return the side of the collision.

        Keyboard arguments:
        x -- the x coordinate of the ball
        y -- the y coordinate of the ball
        paddle -- the Paddle object
        """
        def collision_paddle() -> str:
            """Check if the ball collides with the paddle and return the side of the collision"""
            paddle_x = paddle.xcor()
            if paddle_x + 80 >= x >= paddle_x - 80 and -260 <= y <= -260 + self.speed:
                current_angle = self.heading()
                """Ball moving to the right"""
                direction = 1
                """Ball moving to the left"""
                if current_angle < 270:
                    direction = -1
                if x > paddle_x + 40:
                    if direction > 0:
                        self.setheading(current_angle + 10)
                    else:
                        self.setheading(current_angle - 6)
                elif x < paddle_x - 40:
                    if direction < 0:
                        self.setheading(current_angle - 10)
                    else:
                        self.setheading(current_angle + 6)
                elif x > paddle_x + 20:
                    if direction > 0:
                        self.setheading(current_angle + 7)
                    else:
                        self.setheading(current_angle - 4)
                elif x < paddle_x - 20:
                    if direction < 0:
                        self.setheading(current_angle - 7)
                    else:
                        self.setheading(current_angle + 4)
                return 'top'
            return 'None'

        def collision_bricks() -> str:
            """Check if the ball collides with the bricks and return the side of the collision"""
            for brick, sides in all_bricks.items():
                side = 'None'
                top = sides['top']
                bottom = sides['bottom']
                right = sides['right']
                left = sides['left']
                if right >= x >= left:
                    if (top + self.speed) >= y > top:
                        side = 'bottom'
                    elif (bottom - self.speed) <= y < bottom:
                        side = 'top'
                elif top >= y >= bottom:
                    if (right + self.speed) >= x > right:
                        side = 'left'
                    elif (left - self.speed) <= x < left:
                        side = 'right'
                else:
                    side = 'None'

                if side != 'None':
                    hit_or_destroyed = brick.change_color()
                    sound.play_sound(hit_or_destroyed)
                    self.increase_speed()
                    return side

        side_paddle = collision_paddle()
        side_brick = collision_bricks()

        """Below collisions with the boundaries of the screen are detected."""
        if x >= 585:
            sound.play_sound(2)
            return 'right'
        elif x <= -585:
            sound.play_sound(2)
            return 'left'
        elif y >= 290:
            sound.play_sound(2)
            return 'top'
        if side_paddle != 'None':
            sound.play_sound(1)
            return side_paddle
        elif side_brick != 'None':
            return side_brick
        else:
            return 'None'

    def bounce(self, side: str) -> None:
        """Adjust the ball's direction based on the side of the collision.

        Keyboard arguments:
        side -- the side from which the ball should bounce
        """
        if side not in ['None', last_side[0], 'dummy']:
            old_angle = self.heading()
            direction = 1
            if old_angle > 180:
                direction = -1
            if side == 'right':
                offset = direction * 90
                new_angle = old_angle + offset
            elif side == 'left':
                offset = direction * -90
                new_angle = old_angle + offset
            elif side == 'top':
                new_angle = 360 - old_angle
            elif side == 'bottom':
                new_angle = 360 - old_angle
            else:
                new_angle = old_angle
            last_side[0] = side
            self.setheading(new_angle)

    def move(self, paddle: Paddle) -> None:
        """Bind all the previous methods together and move the ball.

        Keyboard arguments:
        paddle -- the Paddle object
        """
        ball_x = self.xcor()
        ball_y = self.ycor()
        side = self.detect_collision(ball_x, ball_y, paddle)
        self.bounce(side)
        self.forward(self.speed)

    def initialize(self) -> None:
        """Initialize a new round with the paddle in the middle and a random angle for the ball."""
        self.goto(STARTING_POSITION)
        self.setheading(starting_angle())
