import pygame
from pygame.sprite import Group

from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("外星人入侵")

    ship = Ship(ai_setting, screen)
    bullets = Group()
    alien = Alien(ai_setting, screen)
    aliens = Group()
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    play_button = Button(ai_setting, screen, "PLAY")

    gf.create_fleet(ai_setting, screen, ship, aliens)

    while True:
        gf.check_events(ai_setting, screen, ship, bullets, stats, play_button, aliens, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, bullets, ship, aliens, stats, sb)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets, sb)
        gf.update_screen(ai_setting, screen, ship, bullets, aliens, stats, sb, play_button)


run_game()