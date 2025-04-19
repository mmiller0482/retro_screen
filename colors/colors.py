from enum import Enum, auto

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
orange = (255, 165, 0)
purple = (128, 0, 128)
brown = (165, 42, 42)


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
