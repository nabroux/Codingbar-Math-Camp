#Press A to scroll the message collected so far.
from microbit import *
import radio

codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
'.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
'..-', '...-', '.--', '-..-', '-.--', '--..']

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

message = ''

display.scroll('on', loop=True, wait=False)
radio.on()
while True:
    incoming = radio.receive()
    if incoming:
        if incoming in codes:
            index = codes.index(incoming)
            letter = letters[index]
            message += letter
            display.scroll(letter,wait=False)
    
    if button_a.is_pressed():
        display.scroll(message, delay=100)