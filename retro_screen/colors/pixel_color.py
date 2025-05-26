class PixelColor:
    """Represents a single pixel color as RGB"""

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def from_tuple(cls, rgb_tuple):
        """Instantiate from a tuple of RGB values -> (r, g, b)"""
        return cls(*rgb_tuple)

    def tuple(self):
        """Return the color as a tuple of RGB values -> (r, g, b)"""
        return self.red, self.green, self.blue

    def __repr__(self):
        return f"PixelColor(red={self.red}, green={self.green}, blue={self.blue})"
