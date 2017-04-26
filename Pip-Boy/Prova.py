'''
Created on 08 mar 2017

@author: benkhalifayoussef
'''

import smopy
from PIL import Image
from IPython.display import Image
if __name__ == '__main__':
    map = smopy.Map((48., -1., 52., 3.), z=4)
    map.save_png('europe.png')
    Image('europe.png')