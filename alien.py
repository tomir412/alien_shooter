import pygame


class Alien():

    def __init__(self, screen):
        """Initialize the alien and set its starting position"""
        self.screen = screen

        # Load the alien image and get its rect
        self.image = pygame.image.load('images/alien_ch.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each alien at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw an alien at its current location"""
        self.screen.blit(self.image, self.rect)
