import sys

import pygame

from screen import Screen


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
