import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien


def run_game():
    # initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set background color to light-gray
    bg_color = (230, 230, 230)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make an alien
    alien = Alien(screen)

    # Main loop for the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, alien)


run_game()