import pygame
from random import choice
import os
import configparser
from typing import List


def get_path_from_config(key: str) -> str:
    """Return the relative file path to the audio file category folder.

    Keyboard arguments:
    key -- the name of the category folder to be located.
    """
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)
    return config.get('Paths', key)


class Sound:
    """Manage the sounds in the game.

    Attributes:
        sound_dirs (List[str]): a list which contains the paths to sound categories.
    """

    sound_dirs: List[str]

    def __init__(self) -> None:
        """Initialize a Sound object."""
        pygame.mixer.init()
        pygame.mixer.set_num_channels(28)
        hit_sounds_dir = get_path_from_config('hit_sounds_dir')
        paddle_sounds_dir = get_path_from_config('paddle_sounds_dir')
        side_sounds_dir = get_path_from_config('side_sounds_dir')
        brick_destr_sounds_dir = get_path_from_config('brick_destr_sounds_dir')
        win_sound_dir = get_path_from_config('win_sound_dir')
        lose_sound_dir = get_path_from_config('lose_sound_dir')
        lose_life_sound_dir = get_path_from_config('lose_life_sound_dir')
        self.sound_dirs = [hit_sounds_dir, paddle_sounds_dir, side_sounds_dir, brick_destr_sounds_dir, win_sound_dir,
                           lose_sound_dir, lose_life_sound_dir]

    def play_sound(self, sound_nr: int) -> None:
        """Choose a sound category, then randomly select a sound variation and play it."""
        select_sound_category = self.sound_dirs[sound_nr]
        select_random_sound = choice(os.listdir(select_sound_category))
        selected_sound = select_sound_category + select_random_sound
        loaded_sound = pygame.mixer.Sound(selected_sound)
        loaded_sound.play()
