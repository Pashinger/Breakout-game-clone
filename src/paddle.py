from turtle import Turtle

STARTING_POSITION = 0, -270
MOVE_DISTANCE = 40


class Paddle(Turtle):
    """Handle the paddle's appearance and movement."""
    def __init__(self) -> None:
        """Initialize the Paddle object inheriting from the Turtle class."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.resizemode('user')
        self.shapesize(1, 8, 1)
        self.goto(STARTING_POSITION)
        self.shape('square')
        self.color('white')
        self.showturtle()

    def move_left(self) -> None:
        """Move the paddle to the left."""
        if self.distance(-555, -270) > 40:
            self.backward(MOVE_DISTANCE)

    def move_right(self) -> None:
        """Move the paddle to the right."""
        if self.distance(555, -270) > 40:
            self.forward(MOVE_DISTANCE)

    def initialize(self) -> None:
        """Reset the paddle to the starting position."""
        self.goto(STARTING_POSITION)
