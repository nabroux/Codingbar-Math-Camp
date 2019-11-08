from microbit import *

hour = 12
minute = 0

#set hour
display.scroll('set hours.', delay=50, loop=True, wait=False)
while True:
    if button_a.is_pressed():
        if hour == 1:
            hour = 12
        else:
            hour -= 1
        display.scroll(hour, delay=50)
            
    elif button_b.is_pressed():
        if hour == 12:
            hour = 1
        else:
            hour += 1
        display.scroll(hour, delay=50)
        
    elif pin0.is_touched():
        display.scroll('OK', delay=50)
        break
    
#set minute
display.scroll('set minutes.', delay=50, loop=True, wait=False)
while True:
    if button_a.is_pressed():
        if minute == 0:
            minute = 59
        else:
            minute -= 1
        display.scroll(minute, delay=50)
            
    elif button_b.is_pressed():
        if minute == 59:
            minute = 0
        else:
            minute += 1
        display.scroll(minute, delay=50)
        
    elif pin0.is_touched():
        display.scroll('OK', delay=50)
        break
    
#clock is ticking!
while True:
    time = str(hour)+':'+str(minute//10)+str(minute%10)
    display.scroll(time, loop=True, wait=False)
    sleep(60000)
    
    if minute != 59:
        minute += 1
    elif hour != 12:
        hour += 1
        minute = 0
    else:
        hour = 1
        minute = 0
