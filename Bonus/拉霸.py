from microbit import *
import random
money = 200
ylist = [0,0,0]
stake = 10
while True:
    if button_a.was_pressed():
        display.scroll(money,delay = 50)
        stake = 10
    if button_b.was_pressed():
        money -= stake
        for index in range(random.randint(5,20)):           
            display.clear()
            for x in range(1,4):
                y = random.randint(1,3)
                ylist[x-1] = y
                display.set_pixel(x,y,9)
            sleep(100)
        if ylist[0] == ylist[1] and ylist[1] == ylist[2]:
            sleep(500)
            display.scroll("YES!+"+ str(stake*30) + ' You have '+str(money),delay=100,wait=False)
            money += 30*stake
        if money <= 0:
            display.scroll("YOU LOSE--")
            break
    if accelerometer.was_gesture("shake"):
        stake = stake + 10
        display.scroll(stake,delay = 50)
