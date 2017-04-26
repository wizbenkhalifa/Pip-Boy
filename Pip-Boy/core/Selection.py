'''
Created on 13 Apr 2017

@author: WiZ
'''
import pygame
import datetime
import pygame
import config
import os

class Selection():
    def __init__(self, x, y, name, color, screen):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.selected = False
    def render(self):
        label = config.genFont.render(self.name, 1, self.color)
        screen.blit(label, (self.x, self.y))
        if self.selected:
            pygame.draw.line(screen, self.color, (self.x-5, self.y - 2), (self.x + 65 + 3, self.y-2), 2)
            pygame.draw.line(screen, self.color, (self.x-5, self.y - 2), (self.x - 5, self.y+17+2), 2)
            pygame.draw.line(screen, self.color, (self.x-5, self.y + 17 + 2), (self.x + 65 + 3, self.y+17+2), 2)
            pygame.draw.line(screen, self.color, (self.x + 65 + 3, self.y - 2), (self.x + 65 + 3, self.y+2+17), 2)
    def onSelection(self, screen):
        print(self.name)
        pygame.QUIT
        