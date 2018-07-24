import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_setting, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right:
            self.center += self.ai_setting.ship_speed_factor
            print(self.center)
            #if self.center >= self.ai_setting.screen_width:
            if self.rect.right >= self.screen_rect.right:
                self.moving_right = False
        if self.moving_left:
            self.center -= self.ai_setting.ship_speed_factor
            print(self.center)
            #if self.center <= 0:
            if self.rect.left < 0:
                self.moving_left = False

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx