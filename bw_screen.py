from typing import Tuple

from colors.bw_color_map import bw_color_map
from colors.bw_colors import BWColor
from screen import Screen


class BWScreen(Screen):
    DEFAULT_COLOR_MAP: dict[BWColor, Tuple[int, int, int]] = bw_color_map