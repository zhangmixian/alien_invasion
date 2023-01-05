import sys

import pygame


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, ai_settings, ai_ship):
    screen.fill(ai_settings.bg_color)
    ai_ship.blitme()

    pygame.display.flip()
