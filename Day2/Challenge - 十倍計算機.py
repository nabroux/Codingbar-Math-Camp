from microbit import *

index = 1

while True:
    if button_a.is_pressed():
        if index == 1:
            index = 10
        else:
            index -= 1
        display.scroll(index, delay=50)
    if button_b.is_pressed():
        if index == 10:
            index = 1
        else:
            index += 1
        display.scroll(index, delay=50)
    if pin0.is_touched():
        display.scroll(str(index*10), delay=100)
