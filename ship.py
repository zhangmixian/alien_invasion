import pygame.image


class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        # self.center = float(self.rect.centerx)
        self.speed_setting = ai_settings.ship_speed

        self.right_limit = True
        self.left_limit = True


    def update(self):
        if self.rect.right >= self.screen_rect.right :
            self.right_limit = False
        if self.rect.left <= self.screen_rect.left :
            self.left_limit = False

        if self.moving_right and self.right_limit:
            self.rect.centerx += self.speed_setting
            # self.center += self.speed_setting
        if self.moving_left and self.left_limit:
            self.rect.centerx -= self.speed_setting
            # self.center -= self.speed_setting

        self.right_limit=True
        self.left_limit=True

    def blitme(self):
        self.screen.blit(self.image, self.rect)
