import sys
import pygame

from screen import Screen


class ScreenHandler:
    def __init__(self, screen: Screen):
        self._screen = screen

    def run(self):
        clock = pygame.time.Clock()
        FPS = 60

        dot_x = 0
        dot_y = self._screen.height // 2

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update buffer contents
            self._screen.reset_buffer()
            self._screen.buffer[dot_y][dot_x] = (0, 0, 0)

            dot_x = (dot_x + 1) % self._screen.width

            # Render buffer to screen
            self._screen.render()

            clock.tick(FPS)
