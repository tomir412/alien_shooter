import sys

import pygame

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Smooth movement to left and right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False



def update_screen(ai_settings, screen, ship, alien):
    """Update images on the screen"""
    # Redraw the screen each pass trough loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()