import radio, random
from microbit import *

image = Image("99999:"
              "90989:"
              "00799:"
              "99090:"
              "99999")

flash = []
for i in range(9,-1,-1):
    flash.append(image*(i/9))

radio.on()
while True:
    if button_a.was_pressed():
        radio.send('flash')
    incoming = radio.receive()
    if incoming == 'flash':
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send('flash')