from microbit import *

while True:
    c = temperature()
    display.scroll(str(c)+'C')