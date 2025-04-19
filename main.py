import pygame

from bw_screen import BWScreen
from screen import Screen
from a_game import AGame


def main():
    screen = BWScreen()
    screen_handler = AGame(screen)
    screen_handler.run()


if __name__ == "__main__":
    pygame.init()
    main()
