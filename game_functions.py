import sys

import pygame

from bullet import Bullet


def fire_bullet(ai_ship, bullet, ai_settings, screen):
    if len(bullet) < ai_settings.bullet_allow:
        new_bullet = Bullet(ai_settings, screen, ai_ship)
        bullet.add(new_bullet)
def check_event_down(event, ai_ship, bullet, ai_settings, screen):
    if event.key == pygame.K_RIGHT:
        ai_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ai_ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_ship, bullet, ai_settings, screen)

def check_event_up(event, ai_ship):
    if event.key == pygame.K_RIGHT:
        ai_ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ai_ship.moving_left = False


def check_event(ai_ship, screen, bullet, ai_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_down(event, ai_ship, bullet, ai_settings, screen)
        elif event.type == pygame.KEYUP:
            check_event_up(event, ai_ship)


def update_screen(screen, ai_settings, ai_ship, bullet):
    screen.fill(ai_settings.bg_color)
    bullet.update()

    ai_ship.blitme()
    for bullets in bullet.sprites():
        bullets.draw_bullet()

    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
