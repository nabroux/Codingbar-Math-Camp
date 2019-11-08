from microbit import *

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

letters_l = len(letters)
index = 0
result = ''

while True:
    if button_a.was_pressed():
        if index == 0:
            index = letters_l - 1
        else:
            index -= 1
        display.show(letters[index], delay=50)
    elif button_b.was_pressed():
        if index == letters_l - 1:
            index = 0
        else:
            index += 1
        display.show(letters[index], delay=50)
        
    elif pin0.is_touched():
        result += letters[index]
        display.scroll(result, delay=50)
        
    elif accelerometer.is_gesture('shake'):
        display.scroll(result, loop=True, delay=100)
