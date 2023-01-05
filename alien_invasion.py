import pygame

import game_functions
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ai_ship = Ship(screen)

    pygame.display.set_caption("Alien Incision")
    ai_settings.bg_color = (230, 230, 230)

    while True:
        game_functions.check_event()
        game_functions.update_screen(screen, ai_settings, ai_ship)


run_game()
