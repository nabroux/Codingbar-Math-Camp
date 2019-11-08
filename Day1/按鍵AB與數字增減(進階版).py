# Add your Python code here. E.g.
from microbit import *
num = 0

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll(str(num*5))
    elif button_a.is_pressed():
        num -= 1
        display.scroll(str(num))
    elif button_b.is_pressed():
        num += 1
        display.scroll(str(num))
