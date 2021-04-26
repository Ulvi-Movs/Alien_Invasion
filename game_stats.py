# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:35:53 2021

@author: ULVI PC
"""

class GameStats():
    '''Statistics of game'''
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        
        