import sys

import pygame


def check_event_down(event,ai_ship):
        if event.key == pygame.K_RIGHT:
            ai_ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ai_ship.moving_left = True

def check_event_up(event,ai_ship):
        if event.key == pygame.K_RIGHT:
            ai_ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ai_ship.moving_left = False

def check_event(ai_ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_down(event,ai_ship)
        elif event.type == pygame.KEYUP:
            check_event_up(event,ai_ship)

def update_screen(screen, ai_settings, ai_ship):
    screen.fill(ai_settings.bg_color)
    ai_ship.update()
    ai_ship.blitme()

    pygame.display.flip()
