import sys

import pygame

from settings import Settings

def run_game():
    # initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set background color to light-gray
    bg_color = (230, 230, 230)

    # Main loop for the game
    while True:

        # Record keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen each pass trough loop
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()


run_game()