# Add your Python code here. E.g.
from microbit import *
import random

image1 = Image("00000\n"
              "00000\n"
              "00900\n"
              "00000\n"
              "00000")

image2 = Image("00000\n"
              "00000\n"
              "09090\n"
              "00000\n"
              "00000")
              
image3 = Image("00000\n"
              "09090\n"
              "00000\n"
              "00900\n"
              "00000")

image4 = Image("00000\n"
              "09090\n"
              "00000\n"
              "09090\n"
              "00000")
              
image5 = Image("00000\n"
              "09090\n"
              "00900\n"
              "09090\n"
              "00000")
              
image6 = Image("09090\n"
              "00000\n"
              "09090\n"
              "00000\n"
              "09090")
              
dice = random.randint(1,6)

while True:
    gesture = accelerometer.current_gesture()
    
    if gesture == 'shake':
        dice = random.randint(1,6)
    
    if dice == 1:
        display.show(image1)
    elif dice == 2:
        display.show(image2)
    elif dice == 3:
        display.show(image3)
    elif dice == 4:
        display.show(image4)
    elif dice == 5:
        display.show(image5)
    elif dice == 6:
        display.show(image6)
        


