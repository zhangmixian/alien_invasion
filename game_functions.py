import sys

import pygame

from bullet import Bullet
from alien import Alien


def get_number(ai_settings, alien_width):
    availablex = ai_settings.screen_width - 2 * alien_width
    numberx = int(availablex / (2 * alien_width))
    return numberx


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number, number_rows):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * number_rows * alien.rect.height
    alien.rect.x = alien.x
    aliens.add(alien)


def creat_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    numberx = get_number(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for rows in range(number_rows):
        for alien_number in range(numberx):
            creat_alien(ai_settings, screen, aliens, alien_number, rows)


def fire_bullet(ai_ship, bullets, ai_settings, screen):
    if len(bullets) < ai_settings.bullet_allow:
        new_bullet = Bullet(ai_settings, screen, ai_ship)
        bullets.add(new_bullet)


def check_event_down(event, ai_ship, bullet, ai_settings, screen):
    if event.key == pygame.K_RIGHT:
        ai_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ai_ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_ship, bullet, ai_settings, screen)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(screen, ai_settings, ai_ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)

    ai_ship.blitme()
    aliens.draw(screen)
    # for alien in aliens.sprites():
    #     alien.blitme()

    # for alien in aliens.sprites():
    #     screen.blit()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_aliens(aliens):
    check_fleet_edge(aliens)
    aliens.update()


def check_fleet_edge(aliens):
    for alien in aliens:
        if alien.check_edge():
            # change_fleet_direction(aliens,alien.settings)
            alien.rect.y += alien.settings.alien_drop_speed
            alien.settings.fleet_direction *= -1

# def change_fleet_direction(aliens,settings):
#     for alien in aliens.sprites():
#         alien.rect.y += alien.settings.alien_drop_speed
#     settings.fleet_direction *= -1
