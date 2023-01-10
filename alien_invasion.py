import pygame

import game_functions
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ai_ship = Ship(screen,ai_settings)
    bullets=Group()

    pygame.display.set_caption("Alien Incision")
    ai_settings.bg_color = (230, 230, 230)

    while True:
        game_functions.check_event(ai_ship,screen,bullets,ai_settings)
        ai_ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(screen, ai_settings, ai_ship,bullets)




run_game()
