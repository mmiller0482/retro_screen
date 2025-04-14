import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 160, 144
SCALE = 4

# Create the window
screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
pygame.display.set_caption("Sweeping Dot")

# Surface for the bitmap screen
bitmap_surface = pygame.Surface((WIDTH, HEIGHT))

# Frame limiter
clock = pygame.time.Clock()
FPS = 15

# Dot position
dot_x = 0
dot_y = HEIGHT // 2  # Middle of screen vertically

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill screen white
    bitmap_surface.fill((127, 127, 127))

    # Draw the moving black dot
    bitmap_surface.set_at((dot_x, dot_y), (0, 0, 0))

    # Move the dot to the right, wrap around
    dot_x = (dot_x + 1) % WIDTH

    # Scale and draw the bitmap
    scaled_surface = pygame.transform.scale(
        bitmap_surface, (WIDTH * SCALE, HEIGHT * SCALE))
    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()

    # Wait to maintain 15 FPS
    clock.tick(FPS)
