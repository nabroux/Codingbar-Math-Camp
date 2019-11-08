from microbit import *
import radio

radio.on()

codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
'.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
'..-', '...-', '.--', '-..-', '-.--', '--..']

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

current_code = ''

while True:
    incoming = radio.receive()
    if incoming == '-':
        current_code += '-'
        display.scroll('-',delay=50)
    elif incoming == '.':
        current_code += '.'
        display.scroll('.',delay=50)
    elif incoming == '#':
        if current_code in codes:
            index = codes.index(current_code)
            letter = letters[index]
            display.scroll(letter,delay=100, loop=True, wait=False)
        else:
            display.show(Image.SAD)
        current_code = ''