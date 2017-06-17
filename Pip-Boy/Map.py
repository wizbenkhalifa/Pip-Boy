'''
Created on Apr 25, 2017

@author: WiZ
'''
import osmapi
import smopy
import os
from IPython.display import Image
import pygame
from interface.ui import Interface
import requests
import json
"""
import matplotlib.pyplot as plt
import matplotlib.cm
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
"""

import config
class Map():
    def __init__(self, screen):
        self.screen = screen
        self.menu = "MAP"
        self.color = config.COLOR_CURRENT
        self.ui = Interface(self.menu, self.screen)
        self.x = 180
        """
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        self.lat = j['latitude']
        self.lon = j['longitude']
        smopy.TILE_SERVER = "http://tile.basemaps.cartocdn.com/light_all/{z}/{x}/{y}@2x.png"
        smopy.TILE_SIZE = 512
        self.map = smopy.Map((48.7, 2.1, 49., 2.5), z=20)
        self.map.show_ipython()
        self.map.save_png('europe.png')
        """
        #print(self.lat, " - ", self.lon)
        #webview.create_window("https://www.google.it/maps/place/31044+Montebelluna+TV/@45.7752859,12.0083184,13z/data=!3m1!4b1!4m5!3m4!1s0x477924f72ac90249:0x6a7ba9ed2f3d2442!8m2!3d45.775491!4d12.0439904")
    def get_image(self, path):
        _image_library = {}
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
    
    def renderInterface(self):
        if self.color != config.COLOR_CURRENT:
            self.color = config.COLOR_CURRENT
        self.ui.render()
        """image = pygame.transform.scale(self.get_image('europe.png'), (250,200))
        self.screen.blit(image, (30, 30))"""
        pygame.draw.line(self.screen, self.color, (250, config.HEIGHT-30), (290, config.HEIGHT-30), 2)
        pygame.draw.line(self.screen, self.color, (250, config.HEIGHT-30), (250, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (250, config.HEIGHT-12), (290, config.HEIGHT-12), 2)
        pygame.draw.line(self.screen, self.color, (290, config.HEIGHT-30), (290, config.HEIGHT-12), 2)
    def onSelection(self):
        self.selections[self.selectionIndex].onSelection(self.screen)
