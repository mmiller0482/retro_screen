import random
from enum import Enum

from retro_screen.colors.pixel_color import PixelColor


class ColorPalette:
    COLOR_ENUM = None
    BG_COLOR = None

    def __init__(self, color_map: dict[Enum, PixelColor]):
        if self.COLOR_ENUM is None or self.BG_COLOR is None:
            raise NotImplementedError(
                "Developer: Implement COLOR_ENUM and BG_COLOR in concrete classes"
            )
        self._colors = color_map

    def get_rgb(self, color: Enum) -> PixelColor:
        """Gets RGB PixelColor for given color enum"""
        # TODO: What happens when the requested color does not exist?
        return self._colors[color]

    def get_background_enum(self) -> Enum:
        """gets the enum value for assigned background color"""
        return self.BG_COLOR

    def get_background_rgb(self) -> PixelColor:
        """gets the RGB value for assigned background color"""
        return self.get_rgb(self.BG_COLOR)

    def has_color(self, color: Enum) -> bool:
        """Checks if the given color enum is in the palette"""
        return color in self._colors

    def random_color(self) -> Enum:
        """Returns a random color from the palette"""
        return random.choice(list(self._colors.keys()))

    def all_colors(self) -> list[Enum]:
        """Returns a list of all colors in the palette"""
        return list(self._colors.keys())

    def all_rgb_values(self) -> list[PixelColor]:
        """Returns a list of all RGB PixelColor values in the palette"""
        return list(self._colors.values())

    def items(self):
        """Returns a list of (color, PixelColor) tuples"""
        return self._colors.items()

    def __getitem__(self, color: Enum) -> PixelColor:
        """Allows color access like palette[Color.RED]"""
        return self.get_rgb(color)
