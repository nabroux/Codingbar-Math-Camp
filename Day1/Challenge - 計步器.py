from microbit import *

n = 0
display.scroll(n, wait=False, loop=True, delay=50)

while True:
    if accelerometer.was_gesture('shake'):
        n += 1
        display.scroll(n, wait=False, loop=True, delay=50)
    if button_a.is_pressed():
        n = 0
        display.scroll(n, wait=False, loop=True, delay=50)
    
