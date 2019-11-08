# Add your Python code here. E.g.
from microbit import *
import random

image0 = Image("09090\n"
              "09090\n"
              "00900\n"
              "09990\n"
              "09990")
              
image1 = Image("00000\n"
              "09990\n"
              "09990\n"
              "09990\n"
              "00000")
              
image2 = Image("09990\n"
              "09990\n"
              "99990\n"
              "99990\n"
              "09990")

hand = random.randint(0,2)

while True:
    gesture = accelerometer.current_gesture()
    
    if gesture == 'shake':
        hand = random.randint(0,2)
    
    if hand == 0:
        display.show(image0)
    elif hand == 1:
        display.show(image1)
    elif hand == 2:
        display.show(image2)

