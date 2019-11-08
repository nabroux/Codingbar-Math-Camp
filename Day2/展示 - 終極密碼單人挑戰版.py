#press A and B to choose a number
from microbit import *
import random

life = 5
maxi = 50
mini = 1
answer = random.randint(mini+1, maxi-1)
guess = mini + 1

def go():
    global life
    global mini
    global maxi
    global guess
    
    if guess == answer:
        display.show(Image.HAPPY, delay=300)
        display.scroll('You Win!', delay=100)
        life = 0
    elif guess > answer:
        maxi = guess
        guess = maxi - 1
        life -= 1
        display.show(Image.SAD, delay=300)
        display.scroll(str(mini) +' to '+ str(maxi), delay=50)
        display.show([Image.HEART, str(life)], delay=300, clear=True)
    elif guess < answer:
        mini = guess
        guess = mini + 1
        life -= 1
        display.show(Image.SAD, delay=300)
        display.scroll(str(mini) +' to '+ str(maxi), delay=50)
        display.show([Image.HEART, str(life)], delay=300, clear=True)

#main        
display.scroll(str(mini) +' to '+ str(maxi), delay=50)
display.show([Image.HEART, str(life)], delay=300, clear=True)
display.scroll(guess, delay=50)

while life != 0:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(guess, clear=True)
        go()
        display.scroll(guess, delay=50)
       
    elif button_a.is_pressed():
        if guess == mini+1:
            display.scroll(guess, delay=50)
        else:
            guess -= 1
            display.scroll(guess, delay=50)
            
    elif button_b.is_pressed():
        if guess == maxi-1:
            display.show('X')
            display.scroll(guess, delay=50)
        else:
            guess += 1
            display.scroll(guess, delay=50)

#Game over
display.scroll('Game Over!', delay=100)
        
