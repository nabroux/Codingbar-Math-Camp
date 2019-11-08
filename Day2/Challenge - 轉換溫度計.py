# 按鍵A攝氏，按鍵B華氏
from microbit import *

display.scroll('Press A or B', loop=True, delay=100, wait=False)

while True:
    c = temperature()
    f = c * 9/5 + 32
    if button_a.was_pressed():
        display.scroll(c, loop=True, wait=False)
    elif button_b.was_pressed():
        display.scroll(f, loop=True, wait=False)
