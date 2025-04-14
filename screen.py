from typing import Tuple

import pygame


class Screen:
    DEFAULT_WIDTH = 160
    DEFAULT_HEIGHT = 144
    DEFAULT_SCALE = 4
    DEFAULT_BACKGROUND: Tuple[int, int, int] = (127, 127, 127)

    def __init__(
        self,
        caption: str = "Window",
        width: int | None = None,
        height: int | None = None,
        scale: int | None = None,
    ):
        if not pygame.display.get_init():
            raise RuntimeError(
                "pygame.display must be initialized before creating a Screen."
                "Simply call pygame.init() somewhere in your main script.")
        cls = self.__class__
        self.width = width or cls.DEFAULT_WIDTH
        self.height = height or cls.DEFAULT_HEIGHT
        self.scale = scale or cls.DEFAULT_SCALE

        self.window = pygame.display.set_mode(
            (self.width * self.scale, self.height * self.scale)
        )
        pygame.display.set_caption(caption)

        self.surface = pygame.Surface((self.width, self.height))

    def reset_state(self, color: Tuple[int, int, int] | None = None):
        if color is None:
            color = self.DEFAULT_BACKGROUND
        self.surface.fill(color)


if __name__ == "__main__":
    pygame.init()
    screen = Screen()
