from enum import Enum, auto
from typing import Tuple

from retro_screen.colors.default_palette import ColorPalette
from retro_screen.colors.pixel_color import PixelColor

white = PixelColor(255, 255, 255)
black = PixelColor(0, 0, 0)


class BWColor(Enum):
    WHITE = auto()
    BLACK = auto()


class BWColorPalette(ColorPalette):
    COLOR_ENUM = BWColor
    BG_COLOR = BWColor.WHITE

    def __init__(self):
        colors: dict[Enum, PixelColor] = {
            BWColor.BLACK: black,
            BWColor.WHITE: white,
        }

        super().__init__(colors)
