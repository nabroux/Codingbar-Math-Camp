from microbit import *
import music

minute = 0
second = 0

display.scroll('set minutes.', delay=70, loop=True, wait=False)
while True:
    if button_a.is_pressed():
        if minute == 0:
            minute = 0
        else:
            minute -= 1
        display.scroll(minute, delay=50)
        
    elif button_b.is_pressed():
        minute += 1
        display.scroll(minute, delay=50)
        
    elif pin1.is_touched():
        display.scroll('OK', delay=50)
        break

display.scroll('set seconds.', delay=50, loop=True, wait=False)
while True:
    if button_a.is_pressed():
        if second == 0:
            second = 59
        else:
            second -= 1
        display.scroll(second, delay=50)
            
    elif button_b.is_pressed():
        if second == 59:
            second = 0
        else:
            second += 1
        display.scroll(second, delay=50)
        
    elif pin1.is_touched():
        display.scroll('OK', delay=50)
        break
    
#clock is ticking!
while True:
    msg = str(minute)+':'+str(second//10)+str(second%10)
    display.scroll(msg, delay=50, wait=False)
    sleep(1000)
    
    if second != 0:
        second -= 1
    elif minute != 0:
        minute -= 1
        second = 59
    else:
        display.show(Image.MUSIC_QUAVER)
        music.play(music.RINGTONE)
        

