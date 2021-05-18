# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:21:06 20

@author: ULVI PC
"""

import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Class for bullet flight'''
    def __init__(self, ai_settings, screen, ship):
        '''Create a bullet'''
        super(Bullet,self).__init__()
        self.screen = screen
        
        # Create bullet on (0,0) position and bup to the right place
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        '''Boolet movement'''
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color, self.rect)
