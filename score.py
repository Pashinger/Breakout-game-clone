from turtle import Turtle
from sounds import Sound

STARTING_POSITION = 390, 260
sound = Sound()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(STARTING_POSITION)
        self.pendown()
        self.lives = 3
        self.score = 0
        self.write(arg=f'lives: 3 score: 0', font=('Arial', 18, 'bold'))

    # update_score method writes a new score on the screen
    def update_score(self):
        self.clear()
        self.write(arg=f'lives: {self.lives} score: {self.score}', font=('Arial', 18, 'bold'))

    # game_over method subtracts a life and checks if the game should continue
    def game_over(self):
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
