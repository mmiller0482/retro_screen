import sys
import random

import pygame

from retro_screen.screen import Screen


class AGame:
    def __init__(self, screen: Screen):
        self._screen = screen

    def run(self):
        clock = pygame.time.Clock()
        FPS = 60
        pixel_index = 0
        pixel_count = self._screen.width * self._screen.height
        y = 0

        color_list = self._screen.color_palette.all_colors()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            color_choice = random.choice(color_list)

            x = pixel_index % self._screen.width
            y = pixel_index // self._screen.width

            self._screen.set_pixel(x, y, color_choice)
            pixel_index = (pixel_index + 1) % pixel_count

            # Render buffer to screen
            self._screen.render()

            clock.tick(FPS)
