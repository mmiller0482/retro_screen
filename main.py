import pygame

from retro_screen import BWColorPalette
from retro_screen import Screen
from a_game import AGame


def main():
    screen = Screen(color_palette=BWColorPalette())
    screen_handler = AGame(screen)
    screen_handler.run()


if __name__ == "__main__":
    pygame.init()
    main()
