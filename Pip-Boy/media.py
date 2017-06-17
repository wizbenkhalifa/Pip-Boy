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
        self.color = config.COLOR_CURRENT
        self._image_library = {}
        self._date = None
        self.selections = []
        self.songs = []
        self.ui = Interface(self.menu, self.screen)
        self.images = []
        self.selectionIndex = 0
        self.getSongs()
        self.x = 100
        self.selection = 0
        self.switch = Selection(200,50, "Images", self.color)
        self.switch.render()
                
    def renderInterface(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.ui.render()
        self.switch.render()
        y = 50
        i = self.selectionIndex
        if self.selection == 0:
            print(self.selections.__len__())
            while i<self.selectionIndex+10:
                if i< self.selections.__len__():
                    self.selections[i].y = y
                    self.selections[i].render()
                    i += 1
                    y += 20
                else:
                    break
            for s in self.selections:
                s.selected = False
            self.selections[self.selectionIndex].selected = True
        elif self.selection ==1:
            print("Images")
        pygame.draw.line(self.screen, self.color, (102, config.HEIGHT-30), (157, config.HEIGHT-30), 2)
        pygame.draw.line(self.screen, self.color, (102, config.HEIGHT-30), (102, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (102, config.HEIGHT-12), (157, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (157, config.HEIGHT-30), (157, config.HEIGHT-12), 2)
        
    def onSelection(self):
        self.selections[self.selectionIndex].play()
    
    def getSongs(self):
        i = 0
        path = "C:/Users/WiZ/Music"
        try:    
            list = os.listdir(path)
            while i < list.__len__():
                filename, file_extension = os.path.splitext(list[i])
                #print(file_extension)
                if file_extension == ".mp3":
                    if self.selections.__len__() <= 0:
                        self.selections.append(Song(20, 20, filename, self.color))
                    else:
                        self.selections.append(Song(20, self.selections[self.selections.__len__()-1].y+20, filename, self.color))
                        print(self.selections[self.selections.__len__()-1].name)
           while i < list.__len__():
            filename, file_extension = os.path.splitext(list[i])
            #print(file_extension)
            if file_extension == ".mp3":
                if self.selections.__len__() <= 0:
                    self.selections.append(Song(20, 20, filename, self.color))
                else:
                    self.selections.append(Song(20, self.selections[self.selections.__len__()-1].y+20, filename, self.color))
                    print(self.selections[self.selections.__len__()-1].name)
            i += 1 i += 1
        except FileNotFoundError:
            print("Path not avaiable")
        
                
                
class Song():
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.name = name
        self.color = config.COLOR_CURRENT
        self.selected = False
        self.path = "C:/Users/WiZ/Music/" + self.name + ".mp3"
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
        
    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play() 
