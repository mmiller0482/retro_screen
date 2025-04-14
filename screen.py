from typing import Tuple

import pygame


class Screen:
    WIDTH = 160
    HEIGHT = 144
    SCALE = 4
    BACKGROUND: Tuple[int, int, int] = (127, 127, 127)

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
        self.width = width or cls.WIDTH
        self.height = height or cls.HEIGHT
        self.scale = scale or cls.SCALE

        self.window = pygame.display.set_mode(
            (self.width * self.scale, self.height * self.scale)
        )
        pygame.display.set_caption(caption)

        self.surface = pygame.Surface((self.width, self.height))

    def reset_state(self, color: Tuple[int, int, int]):
        self.surface.fill(color)


if __name__ == "__main__":
    pygame.init()
    screen = Screen()
