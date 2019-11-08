#----------------------------學生
from microbit import *
import radio
​
table = [?,?,?,?,?,
         ?,?,?,?,?,
         ?,?,?,?,?,
         ?,?,?,?,?,
         ?,?,?,?,?]

if len(set(table)) != 25:
  display.scroll("Wrong")
else:
    radio.on()
    ​
    while True:
      incoming = radio.receive()
      if incoming:
        incoming = int(incoming)
        for i in table:
          if i == incoming:
            number = table.index(i)
            x = (number % 5)
            y = number // 5
            display.set_pixel(x,y,9)
            break
      
