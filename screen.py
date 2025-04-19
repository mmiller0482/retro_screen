from enum import Enum
from typing import Tuple

import pygame

from colors.color_palette import ColorPalette
from colors.default_palette import DefaultColorPalette


class Screen:
    DEFAULT_WIDTH = 160
    DEFAULT_HEIGHT = 144
    DEFAULT_SCALE = 4
    DEFAULT_BACKGROUND: Tuple[int, int, int] = (127, 127, 127)
    DEFAULT_COLOR_PALETTE: type[ColorPalette] =  DefaultColorPalette

    def __init__(
        self,
        caption: str = "Window",
        width: int | None = None,
        height: int | None = None,
        scale: int | None = None,
        color_palette: ColorPalette | None = None,
    ):
        if not pygame.display.get_init():
            raise RuntimeError(
                "pygame.display must be initialized before creating a Screen. "
                "Call pygame.init() somewhere in your main script."
            )

        cls = self.__class__
        self.width = width or cls.DEFAULT_WIDTH
        self.height = height or cls.DEFAULT_HEIGHT
        self.scale = scale or cls.DEFAULT_SCALE

        self.window = pygame.display.set_mode(
            (self.width * self.scale, self.height * self.scale)
        )
        pygame.display.set_caption(caption)

        self.surface = pygame.Surface((self.width, self.height))

        # Initialize pixel buffer with default background color
        self.buffer: list[list[Tuple[int, int, int]]] = [
            [cls.DEFAULT_BACKGROUND for _ in range(self.width)]
            for _ in range(self.height)
        ]
        self.color_palette = color_palette or cls.DEFAULT_COLOR_PALETTE()

    def reset_buffer(self, color: Tuple[int, int, int] | None = None):
        """Reset the screen buffer to the given color or the default background."""
        if color is None:
            color = self.DEFAULT_BACKGROUND
        for y in range(self.height):
            for x in range(self.width):
                self.buffer[y][x] = color

    def set_pixel(self, x: int, y: int, color: Enum):
        """Set the pixel at the given position to the given color."""
        if not self.color_palette.has_color(color):
            raise ValueError(f"Invalid color: {color}")

        if not 0 <= x < self.width or not 0 <= y < self.height:
            raise IndexError(f"Pixel index out of range: ({x}, {y})")

        self.buffer[y][x] = self.color_palette[color]

    def render(self):
        """Render the current buffer to the display."""
        for y in range(self.height):
            for x in range(self.width):
                self.surface.set_at((x, y), self.buffer[y][x])

        scaled = pygame.transform.scale(
            self.surface,
            (self.width * self.scale, self.height * self.scale),
        )
        self.window.blit(scaled, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = Screen()
