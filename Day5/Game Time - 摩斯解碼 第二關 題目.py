from microbit import *
import radio

radio.on()
display.scroll('on', loop=True, wait=False)
while True:
    sleep(3000)
    radio.config(channel = 7)
    radio.send('-.-. .... .- -. -. . .-..')
    radio.send('... .. -..-')
    sleep(3000)
    radio.config(channel = 6)
    radio.send('-- .. -.-. .-. --- -... .. -')