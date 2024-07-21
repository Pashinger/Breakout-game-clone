from turtle import Turtle

STARTING_POSITION = 0, -270
MOVE_DISTANCE = 40


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.resizemode('user')
        self.shapesize(1, 8, 1)
        self.goto(STARTING_POSITION)
        self.shape('square')
        self.color('white')
        self.showturtle()

    def move_left(self):
        if self.distance(-555, -270) > 40:
            self.backward(MOVE_DISTANCE)

    def move_right(self):
        if self.distance(555, -270) > 40:
            self.forward(MOVE_DISTANCE)

    def initialize(self):
        self.goto(STARTING_POSITION)
