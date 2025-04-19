from enum import Enum, auto
from typing import Tuple

from retro_screen.colors.color_palette import ColorPalette


class Color(Enum):
    WHITE = auto()
    BLACK = auto()
    GRAY = auto()
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    CYAN = auto()
    MAGENTA = auto()
    ORANGE = auto()


class DefaultColorPalette(ColorPalette):
    def __init__(self):
        colors: dict[Enum, Tuple[int, int, int]] = {
            Color.WHITE: (255, 255, 255),
            Color.BLACK: (0, 0, 0),
            Color.GRAY: (128, 128, 128),
            Color.RED: (255, 0, 0),
            Color.GREEN: (0, 255, 0),
            Color.BLUE: (0, 0, 255),
            Color.YELLOW: (255, 255, 0),
            Color.CYAN: (0, 255, 255),
            Color.MAGENTA: (255, 0, 255),
            Color.ORANGE: (255, 165, 0),
        }

        super().__init__(colors)
