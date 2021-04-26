# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 10:41:58 2021

@author: ULVI PC
"""

class Settings():
    '''Save all setings of game'''
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)
        
        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        
        # aliens settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        
        #bullets setings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        
        