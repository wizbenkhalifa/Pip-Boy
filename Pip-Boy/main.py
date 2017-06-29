'''
Created on 5 Apr 2017

@author: WiZ
'''

import pygame
import config
import os
from interface.home import home
from interface.Map import Map
from interface.documents import documents
from interface.media import media
from pygame.time import delay
from interface.Scanlines import Scanlines,Line
from threading import Lock
from interface.Settings import Settings
from interface.Gallery import Gallery
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN)
pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
done = False
selected_menu = 0
global menu_list
menu_list = [home(screen), media(screen), Gallery(screen), Map(screen), Settings(screen)]
if __name__ == '__main__':
    menu_list[selected_menu].renderInterface()
    scanlines = Scanlines(screen)
    while not done:
        rot_cod = [0,0,0]
        rot_cod[0]=GPIO.input(3)
        rot_cod[1]=GPIO.input(5)
        rot_cod[2]=GPIO.input(7)
        print(rot_cod)
        menu_list[selected_menu].renderInterface()
        scanlines.run()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.KEYDOWN | rot_cod == [1,1,0]:
                if event.key == pygame.K_RIGHT:
                    if selected_menu >= menu_list.__len__() - 1:
                        selected_menu = 0
                        menu_list[selected_menu].renderInterface()
                        print("Menu %n %n", selected_menu, menu_list.__len__())
                    else:
                        selected_menu = selected_menu + 1
                        menu_list[selected_menu].renderInterface()
                        print("Menu %n %n", selected_menu, menu_list.__len__())
                if event.key == pygame.K_LEFT | rot_cod == [1,0,1]:
                    if selected_menu <= 0:
                        selected_menu = menu_list.__len__() - 1
                        menu_list[selected_menu].renderInterface()
                        print("Menu %n %n", selected_menu, menu_list.__len__())
                    else:
                        selected_menu = selected_menu - 1
                        menu_list[selected_menu].renderInterface()
                        print("Menu %n %n", selected_menu, menu_list.__len__())
                if event.key == pygame.K_DOWN:
                    if menu_list[selected_menu].selectionIndex < menu_list[selected_menu].selections.__len__() - 1:
                        menu_list[selected_menu].selectionIndex += 1
                    else:
                        menu_list[selected_menu].selectionIndex = 0
                if event.key == pygame.K_UP:
                    if menu_list[selected_menu].selectionIndex > 0:
                        menu_list[selected_menu].selectionIndex -= 1
                    else:
                        menu_list[selected_menu].selectionIndex = 2
                if event.key == pygame.K_RETURN:
                    menu_list[selected_menu].onSelection()
                if event.key == pygame.K_PLUS:
                    if selected_menu == 4:
                        menu_list[selected_menu].onIncrement()
                if event.key == pygame.K_RETURN:
                    if selected_menu == 4:
                        menu_list[selected_menu].onDecrement()
                        
        pygame.display.flip()
        delay(100)
    
