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
import matplotlib.pyplot as plt
import matplotlib.cm
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
class Map():
    def __init__(self, screen):
        self.screen = screen
        self.menu = "MAP"
        self.ui = Interface(self.menu, self.screen)
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
        print(self.lat, " - ", self.lon)
    def get_image(self, path):
        _image_library = {}
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
    
    def renderInterface(self):
        self.ui.render()
        image = pygame.transform.scale(self.get_image('europe.png'), (500,300))
        self.screen.blit(image, (30, 30))
    def onSelection(self):
        self.selections[self.selectionIndex].onSelection(self.screen)