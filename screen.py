from typing import Tuple

import pygame
import sys


class Screen:
    WIDTH = 160
    HEIGHT = 144
    SCALE = 4
    BACKGROUND: Tuple[int, int, int] = (127, 127, 127)

    def __init__(
        self,
        caption: str = "Window",
        width: int = None,
        height: int = None,
        scale: int = None,
    ):
        if width is None:
            width = self.__class__.WIDTH
        if height is None:
            height = self.__class__.HEIGHT
        if scale is None:
            scale = self.__class__.SCALE
        self.width = width
        self.height = height
        self.scale = scale
        pygame.init()
        self.window = pygame.display.set_mode(
            (width * scale, height * scale)
        )  # ← Store this
        pygame.display.set_caption(caption)
        self.surface = pygame.Surface((width, height))

    def reset_state(self, color: Tuple[int, int, int]):
        self.surface.fill(color)


class ScreenHandler:
    def __init__(self, screen: Screen):
        self._screen = screen

    def run(self):

        # Frame limiter
        clock = pygame.time.Clock()
        FPS = 15
        # Dot position
        dot_x = 0
        dot_y = self._screen.height // 2  # Middle of screen vertically

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear the surface with background color
            self._screen.surface.fill(self._screen.BACKGROUND)

            # Draw the moving black dot
            self._screen.surface.set_at((dot_x, dot_y), (0, 0, 0))

            # Move the dot to the right, wrap around
            dot_x = (dot_x + 1) % self._screen.width

            # Scale and draw to display
            scaled_surface = pygame.transform.scale(
                self._screen.surface,
                (
                    self._screen.width * self._screen.scale,
                    self._screen.height * self._screen.scale,
                ),
            )
            self._screen.window.blit(scaled_surface, (0, 0))
            pygame.display.flip()

            clock.tick(FPS)


screen = Screen()
screen_handler = ScreenHandler(screen)
screen_handler.run()
