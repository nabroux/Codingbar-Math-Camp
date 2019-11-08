# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()
while True:
    if button_a.was_pressed():
        radio.send('-')
        display.scroll('-',delay=50)
    elif button_b.was_pressed():
        radio.send('.')
        display.scroll('.',delay=50)
    elif accelerometer.was_gesture("shake"):
        radio.send('#')
        display.scroll('OK',delay=50)