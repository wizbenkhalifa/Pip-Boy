'''
Created on Jun 29, 2017

@author: WiZ
'''

import threading
import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN)

exitFlag = 0

class GPIOT(threading.Thread):
    def __init__(self, left, right):
        threading.Thread.__init__(self)
        self.left = left
        self.right = right
        self.rot_cod = [0,0,0]
    def run(self):
       while True:
            self.rot_cod[0]=GPIO.input(3)
            self.rot_cod[1]=GPIO.input(5)
            self.rot_cod[2]=GPIO.input(7)
            #print(rot_cod)
            if self.rot_cod[2]==0 & self.rot_cod[1]==1:   
                self.left = 1
                print(self.left)
                print(self.right)
            if self.rot_cod[1] == 0 & self.rot_cod[2]==1:
                self.right =1
                print(self.left)
                print(self.right)
            sleep(0.1)
       