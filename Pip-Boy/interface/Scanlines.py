'''
Created on 12 May 2017

@author: WiZ
'''
import threading
import config
import pygame

class Scanlines():
    def __init__(self, screen):
        self.color = config.COLOR_CURRENT
        self.lines = []
        self.nLines = 0
        self.largeLines = []
        self.totLines = 0
        self.screen = screen
    def run(self):
        #print("avvio")
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        if self.nLines == 0:
                self.lines.append(Line(12, 0, self.color, 1))
                self.nLines += 1
                self.totLines += 1
        if self.lines[self.nLines - 1].y > config.WIDTH / 100:
            self.lines.append(Line(12, 0, self.color, 1))
            self.nLines += 1
            self.totLines += 1
            #print("Added line")
        for l in self.lines:
            if l.y >= config.HEIGHT:
                self.lines.remove(l)
                #print("Removed line")
                self.nLines -= 1
            l.y = l.y + 3
            self.screen.blit(l.s, (l.x, l.y))  # (0,0) are the top-left coordinates
            # print("Line", l.y, "Nlines: ", self.nLines)
        
class Line():
    def __init__(self, x, y, color, height):
        self.color = config.COLOR_CURRENT
        self.x = x
        self.y = y
        self.s = pygame.Surface((config.WIDTH - 15, height))  # the size of your rect
        self.s.set_alpha(50)  # alpha level
        self.s.fill(self.color)  # this fills the entire surface
