#Press A to scroll the message collected so far.
from microbit import *
import radio

codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',\
'.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',\
'..-', '...-', '.--', '-..-', '-.--', '--..']

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

result = ''

display.scroll('on', loop=True, wait=False)
radio.on()
radio.config(channel = 6)
while True:
    incoming = radio.receive()
    if incoming:
        incoming_list = incoming.split()
        for text in incoming_list:
            index = codes.index(text)
            letter = letters[index]
            result += letter
        display.scroll(result, delay=100)
        result = ''