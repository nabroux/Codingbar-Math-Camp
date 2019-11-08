from microbit import *
minute = 0
second = 0
while True:
    msg = str(minute)+':'+str(second//10)+str(second%10)
    display.scroll(msg, delay=50, wait=False)
    sleep(1000)
    second += 1
    if second == 60:
        second = 0
        minute += 1
    
    if button_a.is_pressed():
        display.scroll(msg, delay=100, loop=True)
        break
