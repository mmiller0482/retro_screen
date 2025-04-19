import pygame

from colors.bw_palette import BWColorPalette
from screen import Screen
from a_game import AGame


def main():
    screen = Screen(color_palette=BWColorPalette())
    screen_handler = AGame(screen)
    screen_handler.run()


if __name__ == "__main__":
    pygame.init()
    main()
