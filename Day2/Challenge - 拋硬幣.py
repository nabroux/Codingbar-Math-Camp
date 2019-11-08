# Add your Python code here. E.g.
from microbit import *
import random

image0 = Image("09990\n"
              "90009\n"
              "90009\n"
              "90009\n"
              "09990")
              
image1 = Image("09990\n"
              "99999\n"
              "99999\n"
              "99999\n"
              "09990")

coin = random.randint(0,1)

while True:
    gesture = accelerometer.current_gesture()
    
    if gesture == 'shake':
        coin = random.randint(0,1)
    
    if coin == 0:
        display.show(image0)
    else:
        display.show(image1)

