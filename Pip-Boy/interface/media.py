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
        global playing
        playing = "------------------"
        
        """self.switch = Selection(200,50, "Images", self.color)
        self.switch.render()"""
                
    def renderInterface(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.ui.render()
        #self.switch.render()
        y = 50
        i = self.selectionIndex
        if self.selections.__len__()> 0:
            if self.selection == 0:
                #print(self.selections.__len__())
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
        label = config.genFont.render(playing, 1, self.color)
        self.screen.blit(label, (295, 100))
        img = self.get_image("F:/Java/Pip-Boy/images/006-play-button.png")
        print(playing)
        img = pygame.transform.scale(img, (35, 35))
        self.screen.blit(img,(300,55))
        img = self.get_image("F:/Java/Pip-Boy/images/005-pause.png")
        img = pygame.transform.scale(img, (35, 35))
        self.screen.blit(img,(340,55))
        img = self.get_image("F:/Java/Pip-Boy/images/002-stop.png")
        img = pygame.transform.scale(img, (35, 35))
        self.screen.blit(img,(380,55))
        img = self.get_image("F:/Java/Pip-Boy/images/004-speaker.png")
        img = pygame.transform.scale(img, (35, 35))
        self.screen.blit(img,(300,120))
        img = self.get_image("F:/Java/Pip-Boy/images/003-speaker-1.png")
        img = pygame.transform.scale(img, (35, 35))
        self.screen.blit(img,(340,120))
        img = self.get_image("F:/Java/Pip-Boy/images/001-speaker-2.png")
        img = pygame.transform.scale(img, (35, 35))
        self.screen.blit(img,(380,120))
        pygame.draw.line(self.screen, self.color, (102, config.HEIGHT-30), (157, config.HEIGHT-30), 2)
        pygame.draw.line(self.screen, self.color, (102, config.HEIGHT-30), (102, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (102, config.HEIGHT-12), (157, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (157, config.HEIGHT-30), (157, config.HEIGHT-12), 2)
        
    def get_image(self, path):
        try:
            # global _image_library
            image = self._image_library.get(path)
            if image == None:
                    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                    image = pygame.image.load(canonicalized_path)
                    self._image_library[path] = image
        except Exception:
            print("Immagine non trovata")
        return image
    
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
                        #print(self.selections[self.selections.__len__()-1].name)
                i += 1
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
        playing = self.name
        print(playing)
        

