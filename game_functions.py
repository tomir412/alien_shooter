import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship, alien):
    """Update images on the screen"""
    # Redraw the screen each pass trough loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()