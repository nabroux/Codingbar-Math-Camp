# Add your Python code here. E.g.
from microbit import *
import random

hearts = [Image.HEART_SMALL,Image.HEART_SMALL,Image.HEART]

while True:
    display.show(hearts)
    
    if pin0.is_touched():
        telepathy_index = random.randint(0,100)
        for i in range(7):
            display.show(hearts,delay = 100)
        display.scroll(telepathy_index,loop = True)

