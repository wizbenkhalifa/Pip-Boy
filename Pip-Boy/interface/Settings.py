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
        self.fontSize = 15
        self.color_index=0
        self.selections = [Selection(50,50, self.colors[self.color_index], self.color), Selection(50,80, self.fontSize, self.color)]
        self.ui = Interface(self.menu, self.screen)
        self.selectionIndex = 0      
        self.x = 300
                             
    def renderInterface(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.ui.render()
        for s in self.selections:
            s.render()
        for s in self.selections:
            s.selected=False
        self.selections[self.selectionIndex].selected = True
        pygame.draw.line(self.screen, self.color, (315, config.HEIGHT-30), (394, config.HEIGHT-30), 2)
        pygame.draw.line(self.screen, self.color, (315, config.HEIGHT-30), (315, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (315, config.HEIGHT-12), (394, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (394, config.HEIGHT-30), (394, config.HEIGHT-12), 2)
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
            
    def onIncrement(self):
        if self.selectionIndex == 1:
            if self.fontSize <20:
                self.size +=1
            else:
                self.fontSize = 15
            config.genFont = pygame.font.Font('monofonto.ttf', self.fontSize)
            
    def onDecrement(self):
        if self.selectionIndex == 1:
            if self.fontSize >15:
                print(self.fontSize)
                self.fontSize -=1
            else:
                self.fontSize = 20
            config.genFont = pygame.font.Font('monofonto.ttf', self.fontSize)
            
    def get_image(self, path):
        # global _image_library
        image = self._image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                self._image_library[path] = image
        return image