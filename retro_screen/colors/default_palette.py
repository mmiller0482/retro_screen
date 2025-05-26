from enum import Enum, auto

from retro_screen.colors.color_palette import ColorPalette
from retro_screen.colors.pixel_color import PixelColor


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
    BG_COLOR = COLOR_ENUM.WHITE

    def __init__(self):
        colors: dict[Enum, PixelColor] = {
            DefaultColor.WHITE: PixelColor(255, 255, 255),
            DefaultColor.BLACK: PixelColor(0, 0, 0),
            DefaultColor.GRAY: PixelColor(128, 128, 128),
            DefaultColor.RED: PixelColor(255, 0, 0),
            DefaultColor.GREEN: PixelColor(0, 255, 0),
            DefaultColor.BLUE: PixelColor(0, 0, 255),
            DefaultColor.YELLOW: PixelColor(255, 255, 0),
            DefaultColor.CYAN: PixelColor(0, 255, 255),
            DefaultColor.MAGENTA: PixelColor(255, 0, 255),
            DefaultColor.ORANGE: PixelColor(255, 165, 0),
        }

        super().__init__(colors)
