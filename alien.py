import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.setting = ai_settings
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)
