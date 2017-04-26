'''
Created on Apr 25, 2017

@author: WiZ
'''
import osmapi
import smopy
from IPython.display import Image
import pygame
class Map():
    def __init__(self, screen):
        self.screen = screen
        map = smopy.Map((42., -1., 55., 3.), z=4)
        image = pygame.transform.scale(map.show_ipython(), (100,100))
        self.screen.blit(image, (10, 10))
        