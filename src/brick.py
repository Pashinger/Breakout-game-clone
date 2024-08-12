from turtle import Turtle

STARTING_POSITION = (-560, 0)
MOVE_DISTANCE = 40
COLORS = ['purple', 'blue', 'green', 'yellow', 'red']
bricks_hit = []
score_list = []
all_bricks = {}


def make_wall() -> None:
    """Create a wall of bricks and store their positions in all_bricks dictionary"""
    color_nr = 0
    brick_x = -555
    brick_y = 0
    for _ in range(0, 60):
        if _ % 12 == 0 and _ != 0:
            brick_x = -555
            brick_y += 50
            color_nr += 1
        brick = Brick(color_nr)
        all_bricks[brick] = {'top': brick_y + 20, 'bottom': brick_y - 20, 'right': brick_x + 40, 'left': brick_x - 40}
        brick.move(brick_x, brick_y)
        brick_x += 100


class Brick(Turtle):
    """Manage the properties and movement of the bricks."""
    def __init__(self, row_nr: int) -> None:
        """Initialize a Brick object inheriting from the Turtle class.

        Keyboard arguments:
        row_nr -- indicates the color a brick should have based on the row it is in
        """
        super().__init__()
        self.hideturtle()
        self.color(COLORS[row_nr])
        self.penup()
        self.resizemode('user')
        self.shapesize(4, 2, 1)
        self.shape('square')
        self.setheading(90)
        self.showturtle()

    def move(self, x: int, y: int) -> None:
        """Move the brick object to other coordinates."""
        self.goto(x, y)

    def change_color(self) -> int:
        """Change the color of a brick and hide it when 'destroyed'"""
        bricks_hit.append(0)
        new_index = COLORS.index(self.color()[0]) - 1
        if new_index < 0:
            self.hideturtle()
            all_bricks.pop(self)
            return 3
        else:
            self.color(COLORS[new_index])
            return 0
