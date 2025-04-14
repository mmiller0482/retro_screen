import pygame

from screen import Screen
from screen_handler import ScreenHandler


def main():
    screen = Screen()
    screen_handler = ScreenHandler(screen)
    screen_handler.run()


if __name__ == "__main__":
    pygame.init()
    main()
