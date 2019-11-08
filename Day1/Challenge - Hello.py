from microbit import *

delay = 10
while True:
    display.scroll('Hello', delay=delay)
    delay += 50
