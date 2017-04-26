'''
Created on 07 apr 2017

@author: benkhalifayoussef
'''
import datetime
import pygame
import config
import os
from interface.ui import Interface
class documents(object):

    def __init__(self, screen):
        self.screen = screen
        self.menu = "DOCUMENTS"
        self.color = (26, 255, 128)
        self.selections = []
        self.ui = Interface(self.menu, self.screen)
    
    def renderInterface(self):
        self.ui.render()
        #scanlines = Scanlines(800, 480, 3, 1, [(0, 13, 3, 50), (6, 42, 22, 100), (0, 13, 3, 50)])
        #scanlines.render(5)
    
