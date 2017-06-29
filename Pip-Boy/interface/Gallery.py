'''
Created on 18 May 2017

@author: WiZ
'''
import pygame
import config
import os
import datetime
from interface.ui import Interface
from interface.ui import Selection
import pyowm
class Gallery(object):
   
    def __init__(self, screen):
        self.screen = screen
        self.menu = "GALLERY"
        self.font = pygame.font.Font('monofonto.ttf', 18)
        self.color = config.COLOR_CURRENT
        self._image_library = {}
        self._date = None
        self.selections = [Selection(50,50, "Gallery", self.color)]
        self.ui = Interface(self.menu, self.screen)
        self.selectionIndex = 0
        self.x = 250
                            
    def renderInterface(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.ui.render()
       
        for s in self.selections:
            s.render()
        for s in self.selections:
            s.selected=False
        self.selections[self.selectionIndex].selected = True
        pygame.draw.line(self.screen, self.color, (178, config.HEIGHT-30), (232, config.HEIGHT-30), 2)
        pygame.draw.line(self.screen, self.color, (178, config.HEIGHT-30), (178, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (178, config.HEIGHT-12), (232, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (232, config.HEIGHT-30), (232, config.HEIGHT-12), 2)
        #scanlines = Scanlines(800, 480, 3, 1, [(0, 13, 3, 50), (6, 42, 22, 100), (0, 13, 3, 50)])
        #scanlines.render(5)
    def onSelection(self):
        self.selections[self.selectionIndex].onSelection(self.screen)
    
    def get_image(self, path):
        # global _image_library
        image = self._image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                self._image_library[path] = image
        return image
    
class Image():
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.image = image
        self.selected = False
        self.path = "C:/Users/WiZ/Images/" + self.name + ".mp3"
    def render(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        if len(self.name) > 30:
            self.name = self.name[:-(len(self.name) - 30)]
        label = config.genFont.render(self.name, 1, self.color)
        screen.blit(label, (self.x, self.y))
        if self.selected:
            pygame.draw.line(screen, self.color, (self.x - 5, self.y - 2), (self.x + 250 + 3, self.y - 2), 2)
            pygame.draw.line(screen, self.color, (self.x - 5, self.y - 2), (self.x - 5, self.y + 17 + 2), 2)
            pygame.draw.line(screen, self.color, (self.x - 5, self.y + 17 + 2), (self.x + 250 + 3, self.y + 17 + 2), 2)
            
            pygame.draw.line(screen, self.color, (self.x + 250 + 3, self.y - 2), (self.x + 250 + 3, self.y + 2 + 17), 2)
    def onSelection(self, screen):
        #print(self.name)
        pygame.quit()
        
