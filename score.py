from turtle import Turtle
from sounds import Sound

STARTING_POSITION = 390, 260
sound = Sound()


class Score(Turtle):
    """Manage the display of the score and the remaining lives."""

    lives: int
    score: int

    def __init__(self):
        """Initialize a Score object inheriting from the Turtle class."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(STARTING_POSITION)
        self.pendown()
        self.lives = 3
        self.score = 0
        self.write(arg=f'lives: 3 score: 0', font=('Arial', 18, 'bold'))

    def update_score(self) -> None:
        """Write a new score on the screen."""
        self.clear()
        self.write(arg=f'lives: {self.lives} score: {self.score}', font=('Arial', 18, 'bold'))

    def game_over(self) -> bool:
        """Subtract a life and check if the game should continue. Display the final score."""
        self.lives -= 1
        if self.lives == 0:
            self.clear()
            self.penup()
            self.goto(0, -160)
            self.pendown()
            final_score = self.score
            text = f'GAME OVER\nfinal score: {final_score}'
            if final_score == 180:
                sound.play_sound(4)
                text = f'YOU WON!!!\nfinal score: {final_score}'
            else:
                sound.play_sound(5)
            self.write(arg=text, align='center', font=('Arial', 40, 'normal'))
            return False
        else:
            self.update_score()
            sound.play_sound(6)
            return True
