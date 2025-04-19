import random
from enum import Enum
from typing import Tuple


class ColorPalette:
    def __init__(self, color_map: dict[Enum, Tuple[int, int, int]]):
        self._colors = color_map

    def get_rgb(self, color: Enum) -> Tuple[int, int, int]:
        return self._colors[color]

    def has_color(self, color: Enum) -> bool:
        return color in self._colors

    def random_color(self) -> Enum:
        return random.choice(list(self._colors.keys()))

    def all_colors(self) -> list[Enum]:
        return list(self._colors.keys())

    def all_rgb_values(self) -> list[Tuple[int, int, int]]:
        return list(self._colors.values())

    def items(self):
        return self._colors.items()

    def __getitem__(self, color: Enum) -> Tuple[int, int, int]:
        """Allows color access like palette[Color.RED]"""
        return self.get_rgb(color)