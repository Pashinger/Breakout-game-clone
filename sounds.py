import threading
import pygame
import os
from random import choice


class Sound():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(28)
        hit_sounds_dir = 'C:/Users/hp-pc/PycharmProjects/day-87-breakout-game/venv/sounds/brick hit/'
        paddle_sounds_dir = 'C:/Users/hp-pc/PycharmProjects/day-87-breakout-game/venv/sounds/paddle/'
        side_sounds_dir = 'C:/Users/hp-pc/PycharmProjects/day-87-breakout-game/venv/sounds/side hit/'
        brick_destr_sounds_dir = 'C:/Users/hp-pc/PycharmProjects/day-87-breakout-game/venv/sounds/brick destroyed/'
        win_sound_dir = 'C:/Users/hp-pc/PycharmProjects/day-87-breakout-game/venv/sounds/win/'
        lose_sound_dir = 'C:/Users/hp-pc/PycharmProjects/day-87-breakout-game/venv/sounds/lose/'
        lose_life_sound_dir = 'C:/Users/hp-pc/PycharmProjects/day-87-breakout-game/venv/sounds/life lost/'
        self.sound_dirs = [hit_sounds_dir, paddle_sounds_dir, side_sounds_dir, brick_destr_sounds_dir, win_sound_dir,
                           lose_sound_dir, lose_life_sound_dir]

    def play_sound(self, sound_nr):
        select_sound_category = self.sound_dirs[sound_nr]
        select_random_sound = choice(os.listdir(select_sound_category))
        selected_sound = select_sound_category + select_random_sound
        loaded_sound = pygame.mixer.Sound(selected_sound)
        loaded_sound.play()

