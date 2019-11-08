from microbit import *
import random

nums = []

display.scroll('press A to get a number', loop=True, wait=False, delay=100)
while True:
    if button_a.was_pressed():
        while True:
            num = random.randint(1,30)
            if num not in nums:
                display.scroll(num, loop=True, wait=False)
                nums.append(num)
                break
    if len(nums) >= 30:
        break