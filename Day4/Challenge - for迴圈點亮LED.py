from microbit import *

for x in range(5):
    for y in range(5):
        display.set_pixel(x,y,9)
        sleep(200)