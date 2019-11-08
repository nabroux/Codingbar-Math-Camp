from microbit import *
import random, music

answer = random.randint(1,2)

while True:
    if answer == 1:
        if pin1.is_touched() and pin2.is_touched():
            display.show(Image.SURPRISED)
        elif not pin1.is_touched():
            display.show(Image.HAPPY)
            music.play(music.POWER_UP)
        elif not pin2.is_touched():
            display.show(Image.SAD)
            music.play(music.WAWAWAWAA)
            
    elif answer == 2:
        if pin1.is_touched() and pin2.is_touched():
            display.show(Image.SURPRISED)
        elif not pin1.is_touched():
            display.show(Image.SAD)
            music.play(music.WAWAWAWAA)
        elif not pin2.is_touched():
            display.show(Image.HAPPY)
            music.play(music.POWER_UP)
        