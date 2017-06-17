'''
Created on 07 apr 2017

@author: benkhalifayoussef
'''

import pygame
import config
import os
import datetime
from interface.ui import Interface
from interface.ui import Selection
import pyowm
class home(object):
   
    def __init__(self, screen):
        self.screen = screen
        self.menu = "HOME"
        self.font = pygame.font.Font('monofonto.ttf', 18)
        self.color = config.COLOR_CURRENT
        self._image_library = {}
        self._date = None
        self.selections = [Selection(50,50, "SHUTDOWN", self.color), Selection(50,100, "RESTART", self.color), Selection(50,150, "SLEEP", self.color)]
        self.ui = Interface(self.menu, self.screen)
        self.selectionIndex = 0
        self.getWeather()
        self.x = 20
                            
    def renderInterface(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.ui.render()
        for s in self.selections:
            s.render()
        for s in self.selections:
            s.selected=False
        self.selections[self.selectionIndex].selected = True
        self.printWeather()
        pygame.draw.line(self.screen, self.color, (30, config.HEIGHT-30), (77, config.HEIGHT-30), 2)
        pygame.draw.line(self.screen, self.color, (30, config.HEIGHT-30), (30, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (30, config.HEIGHT-12), (77, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (77, config.HEIGHT-30), (77, config.HEIGHT-12), 2)
        #scanlines = Scanlines(800, 480, 3, 1, [(0, 13, 3, 50), (6, 42, 22, 100), (0, 13, 3, 50)])
        #scanlines.render(5)
    def onSelection(self):
        self.selections[self.selectionIndex].onSelection(self.screen)
    
    def printWeather(self):
        label = self.font.render(self.weather, 1, self.color)
        self.screen.blit(label, (200, 200))
        """try:
            #img = img=pygame.image.load(config.WEATHER_ICON[self.weather])
            #img = pygame.transform.scale(img, (150, 150))
            #self.screen.blit(img,(275,25))
            
        except KeyError:
            print("Immagine non trovata")
        """
        label = self.font.render(self.temperature, 1, self.color)
        self.screen.blit(label, (240, 200))
    def get_image(self, path):
        # global _image_library
        image = self._image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                self._image_library[path] = image
        return image
    
        
    def getWeather(self):
        owm = pyowm.OWM('1b0800976558d34e9dfd441c89a6d0e0')  # You MUST provide a valid API key
        observation = owm.weather_at_place('Montebelluna,it')
        w = observation.get_weather()
        s = str(w).split("status=")
        weather = s[s.__len__()-1]
        self.weather = weather.replace(">", "")
        temp = str(w.get_temperature('celsius')).split(",")
        self.temperature = temp[0].split(":")[1]
        self.tMax = temp[1].split(":")[1]
        self.tMin = temp[2].split(":")[1]
        #print(weather," ",temperature,"-",tMax,"-",tMin)
    