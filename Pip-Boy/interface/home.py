'''
Created on 07 apr 2017

@author: benkhalifayoussef
'''
import pygame
import config
import os
import datetime
from interface.ui import Scanlines
from interface.ui import Interface
from interface.ui import Selection
class home(object):
   
    def __init__(self, screen):
        self.screen = screen
        self.menu = "HOME"
        self.color = (26, 255, 128)
        self._image_library = {}
        self._date = None
        self.selections = [Selection(50,50, "SHUTDOWN", self.color), Selection(50,100, "RESTART", self.color), Selection(50,150, "SLEEP", self.color)]
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
        self.selections[self.selectionIndex].onSelection(self.screen)
    
    