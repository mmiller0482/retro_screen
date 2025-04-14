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
        width: int = None,
        height: int = None,
        scale: int = None,
    ):
        if width is None:
            width = self.__class__.WIDTH
        if height is None:
            height = self.__class__.HEIGHT
        if scale is None:
            scale = self.__class__.SCALE
        self.width = width
        self.height = height
        self.scale = scale
        pygame.init()
        self.window = pygame.display.set_mode(
            (width * scale, height * scale)
        )  # ← Store this
        pygame.display.set_caption(caption)
        self.surface = pygame.Surface((width, height))

    def reset_state(self, color: Tuple[int, int, int]):
        self.surface.fill(color)




