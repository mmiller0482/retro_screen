from enum import Enum, auto
from typing import Tuple

from retro_screen.colors.color_palette import ColorPalette


class DefaultColor(Enum):
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
    COLOR_ENUM = DefaultColor

    def __init__(self):
        colors: dict[Enum, Tuple[int, int, int]] = {
            DefaultColor.WHITE: (255, 255, 255),
            DefaultColor.BLACK: (0, 0, 0),
            DefaultColor.GRAY: (128, 128, 128),
            DefaultColor.RED: (255, 0, 0),
            DefaultColor.GREEN: (0, 255, 0),
            DefaultColor.BLUE: (0, 0, 255),
            DefaultColor.YELLOW: (255, 255, 0),
            DefaultColor.CYAN: (0, 255, 255),
            DefaultColor.MAGENTA: (255, 0, 255),
            DefaultColor.ORANGE: (255, 165, 0),
        }

        super().__init__(colors)
