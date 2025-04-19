from enum import Enum, auto
from typing import Tuple

from retro_screen.colors.default_palette import ColorPalette

white = (255, 255, 255)
black = (0, 0, 0)


class BWColor(Enum):
    WHITE = auto()
    BLACK = auto()


class BWColorPalette(ColorPalette):
    COLOR_ENUM = BWColor

    def __init__(self):
        colors: dict[Enum, Tuple[int, int, int]] = {
            BWColor.BLACK: black,
            BWColor.WHITE: white,
        }

        super().__init__(colors)
