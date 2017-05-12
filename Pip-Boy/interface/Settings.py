'''
Created on 12 May 2017

@author: WiZ
'''

import pygame
import config
import os
import datetime
from interface.ui import Interface
from interface.ui import Selection
import pyowm
class Settings(object):
   
    def __init__(self, screen):
        self.screen = screen
        self.menu = "SETTINGS"
        self.font = pygame.font.Font('monofonto.ttf', 18)
        self.color = config.COLOR_CURRENT
        self._image_library = {}
        self._date = None
        self.colors = ['GREEN', 'BLUE', 'YELLOW']
        self.color_index=0
        self.selections = [Selection(50,50, self.colors[self.color_index], self.color)]
        self.ui = Interface(self.menu, self.screen)
        self.selectionIndex = 0      
                             
    def renderInterface(self):
        self.ui.render()
        for s in self.selections:
            s.render()
        for s in self.selections:
            s.selected=False
        self.selections[self.selectionIndex].selected = True
        #scanlines = Scanlines(800, 480, 3, 1, [(0, 13, 3, 50), (6, 42, 22, 100), (0, 13, 3, 50)])
        #scanlines.render(5)
        
    def onSelection(self):
        if self.selectionIndex == 0:
            self.color_index+=1
            if self.color_index > 2:
                self.color_index = 0
            self.selections[self.selectionIndex].name =self.colors[self.color_index]
            config.COLOR_CURRENT = config.COLORS[self.color_index]
            self.color = config.COLOR_CURRENT
            self.ui.color = config.COLOR_CURRENT
    def get_image(self, path):
        # global _image_library
        image = self._image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                self._image_library[path] = image
        return image