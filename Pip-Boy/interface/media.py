'''
Created on 07 apr 2017

@author: benkhalifayoussef
'''

import pygame
import datetime
import pygame
import config
import os
from pygame import mixer
from interface.ui import Interface, Selection
class media(object):
    
    def __init__(self, screen2):
        self.screen = screen2
        global screen
        screen = self.screen
        self.menu = "MEDIA"
        self.color = (26, 255, 128)
        self._image_library = {}
        self._date = None
        self.selections = []
        self.songs = []
        self.ui = Interface(self.menu, self.screen)
        self.selectionIndex = 0
        self.getSongs()
                
    def renderInterface(self):
        self.ui.render()
        y = 50
        i = self.selectionIndex
        while i<self.selectionIndex+10:
            self.selections[i].y = y
            self.selections[i].render()
            i += 1
            y += 20
        for s in self.selections:
            s.selected = False
        print(self.selectionIndex)
        self.selections[self.selectionIndex].selected = True
        # scanlines = Scanlines(800, 480, 3, 1, [(0, 13, 3, 50), (6, 42, 22, 100), (0, 13, 3, 50)])
        # scanlines.render(5)
    def onSelection(self):
        self.selections[self.selectionIndex].play()
    
    def getSongs(self):
        i = 0
        path = "C:/Users/WiZ/Music"
        list = os.listdir(path)
        while i < list.__len__():
            filename, file_extension = os.path.splitext(list[i])
            print(file_extension)
            if file_extension == ".mp3":
                if self.selections.__len__() <= 0:
                    self.selections.append(Song(20, 20, filename, self.color))
                else:
                    self.selections.append(Song(20, self.selections[self.selections.__len__()-1].y+20, filename, self.color))
                    print(self.selections[self.selections.__len__()-1].name)
            i += 1
                
class Song():
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.selected = False
        self.path = "C:/Users/WiZ/Music/" + self.name + ".mp3"
    def render(self):
        label = config.genFont.render(self.name, 1, self.color)
        screen.blit(label, (self.x, self.y))
        if self.selected:
            pygame.draw.line(screen, self.color, (self.x - 5, self.y - 2), (self.x + 100 + 3, self.y - 2), 2)
            pygame.draw.line(screen, self.color, (self.x - 5, self.y - 2), (self.x - 5, self.y + 17 + 2), 2)
            pygame.draw.line(screen, self.color, (self.x - 5, self.y + 17 + 2), (self.x + 100 + 3, self.y + 17 + 2), 2)
            
            pygame.draw.line(screen, self.color, (self.x + 100 + 3, self.y - 2), (self.x + 100 + 3, self.y + 2 + 17), 2)
    def onSelection(self, screen):
        print(self.name)
        pygame.quit()
        
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play() 
