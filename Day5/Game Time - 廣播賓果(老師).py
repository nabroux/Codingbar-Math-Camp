#----------------------------老師
from microbit import *
import radio
​
radio.on()
choose = [x for x in range(1,31)]
index = 0
display.show(str(choose[index]))
while True:
  if button_a.was_pressed():
    index += 1
    if index >= len(choose):
      index = 0
    display.show(str(choose[index]))
    sleep(100)
    
  if button_b.was_pressed():
    radio.send(str(choose[index]))
    del choose[index]
    index = 0
    display.show(str(choose[index]))
    sleep(100)
