import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    # initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set background color to light-gray
    bg_color = (230, 230, 230)

    # Make a ship
    ship = Ship(screen)

    # Main loop for the game
    while True:

        # Record keyboard and mouse events
        gf.check_events()

        # Redraw the screen each pass trough loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


run_game()