'''
Created on Apr 9, 2017

@author: WiZ
'''

import pygame
import datetime
import pygame
import config
import os
from pygame.time import delay
import threading
from asyncio.tasks import sleep


class Interface():
    def __init__(self, maintxt, screen2):
        self.maintxt = maintxt
        self.menuList = ["Home", "Media", "Gallery", "Map", "Settings"]
        self.font = pygame.font.Font('monofonto.ttf', 18)
        self.font2 = pygame.font.Font('monofonto.ttf', 15)
        global screen
        screen = screen2
        self.color = config.COLOR_CURRENT
        self._image_library = {}
        self._date = None
        self.date = datetime.datetime.now().strftime("%d.%m.%y|%H:%M:%S")
        self.time = ""
        self.day = ""
        
    def render(self):
        new_date = datetime.datetime.now().strftime("%d.%m.%y|%H:%M:%S")
        if self.date != new_date:
            self.date = new_date
            self.time = self.date.split("|")[1]
            self.day = self.date.split("|")[0]
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.background()
        self.interface()
        self.texts()
    """   
    def update(self):
        new_date = datetime.datetime.now().strftime("%d.%m.%y.%H:%M:%S")
        if self.date != new_date:
            label = self.font.render(new_date, 1, self.color)
            screen.blit(label, (250, 10))
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.background()
        self.scanlines.run()
        self.interface()
        self.texts()
    """
    def texts(self):
            weekdays = ["Monday", "Tuesday", "Wensday", "Thursday", "Friday", "Saturday", "Sunday"]
            #Main text
            label = self.font.render(self.maintxt, 1, self.color)
            screen.blit(label, (40, 5))
            #TIME
            date = weekdays[datetime.datetime.today().weekday()] + " " + self.day 
            label = self.font2.render(date, 1, self.color)
            screen.blit(label, (330, 18))
            label = self.font2.render(self.time, 1, self.color)
            screen.blit(label, (250, 18))
            x = 40
            y = config.HEIGHT - 30
            i = 0
            i=0
            pygame.draw.line(screen, self.color, (20, config.HEIGHT-20), (20, config.HEIGHT-30), 2)
            pygame.draw.line(screen, self.color, (20, config.HEIGHT-20), (30, config.HEIGHT-20), 2)
            while i < self.menuList.__len__():
                label = self.font2.render(self.menuList[i], 1, self.color)
                screen.blit(label, (x, y))
                pygame.draw.line(screen, self.color, ( x+(len(self.menuList[i])*10), config.HEIGHT-20), (x + (len(self.menuList[i]) * 5) + 40, config.HEIGHT-20), 2)
                try:
                    x = x + (len(self.menuList[i]) * 5) + 50
                except IndexError :
                    print("")
                i +=1
            pygame.draw.line(screen, self.color, (x-20, config.HEIGHT-20), (config.WIDTH-25, config.HEIGHT-20), 2)
            pygame.draw.line(screen, self.color, (config.WIDTH-25, config.HEIGHT-20), (config.WIDTH-25, config.HEIGHT-30), 2)
        
    def interface(self):
        # screen.fill((0, 0, 0))
        # LINEE ALTE
        # VERTICALE
        pygame.draw.line(screen, self.color, (20, 15), (20, 35), 2)
        pygame.draw.line(screen, self.color, (200, 15), (200, 35), 2)
        pygame.draw.line(screen, self.color, (320, 15), (320, 35), 2)
        pygame.draw.line(screen, self.color, (config.WIDTH - 20, 15), (config.WIDTH - 20, 35), 2)
        
        # ORIZZONATALE
        pygame.draw.line(screen, self.color, (20, 15), (30, 15), 2)
        pygame.draw.line(screen, self.color, (100, 15), (200, 15), 2)
        pygame.draw.line(screen, self.color, (205, 15), (320, 15), 2)
        pygame.draw.line(screen, self.color, (325, 15), (config.WIDTH - 20, 15), 2)
        
        # LINEE BASSE
        """
        pygame.draw.line(screen, self.color, (78, config.HEIGHT-20), (108, config.HEIGHT-20), 2)
        pygame.draw.line(screen, self.color, (160, config.HEIGHT-20), (183, config.HEIGHT-20), 2)
        pygame.draw.line(screen, self.color, (235, config.HEIGHT-20), (250, config.HEIGHT-20), 2)
        """
    def background(self):
        image = pygame.transform.scale(self.get_image('images/border.png'), (config.WIDTH, config.HEIGHT))
        screen.blit(image, (10, 10))
        image = pygame.transform.scale(self.get_image('images/overlay.png'), (config.WIDTH, config.HEIGHT))
        screen.blit(image, (0, 0))
        
    
    def get_image(self, path):
        # global _image_library
        image = self._image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                self._image_library[path] = image
        return image
    
    
class Selection():
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.name = name
        self.color = config.COLOR_CURRENT
        self.selected = False
    def render(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        label = config.genFont.render(str(self.name), 1, self.color)
        screen.blit(label, (self.x, self.y))
        if self.selected:
            pygame.draw.line(screen, self.color, (self.x - 5, self.y - 2), (self.x + 65 + 3, self.y - 2), 2)
            pygame.draw.line(screen, self.color, (self.x - 5, self.y - 2), (self.x - 5, self.y + 17 + 2), 2)
            pygame.draw.line(screen, self.color, (self.x - 5, self.y + 17 + 2), (self.x + 65 + 3, self.y + 17 + 2), 2)
            pygame.draw.line(screen, self.color, (self.x + 65 + 3, self.y - 2), (self.x + 65 + 3, self.y + 2 + 17), 2)
    def onSelection(self, screen):
        print(self.name)
        pygame.quit()
        
