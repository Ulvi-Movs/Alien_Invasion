# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:02:41 2021

@author: ULVI PC
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''Initialazie of alien'''
    def __init__(self,ai_settings, screen):
        '''Download images for sip'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/hero.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)




    def update(self):
        '''update ship position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
    
        self.rect.centerx = self.center
    
    
    
    
    def blitme(self):
        '''draw ship in posiction'''
        self.screen.blit(self.image, self.rect)