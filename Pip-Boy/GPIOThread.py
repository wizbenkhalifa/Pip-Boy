'''
Created on Jun 29, 2017

@author: WiZ
'''

import threading
import time

from time import sleep


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
            if self.rot_cod[2]==0 and self.rot_cod[1]==1:   
                left = 1
                
            if self.rot_cod[1] == 0 and self.rot_cod[2]==1:
                right =1
                
       