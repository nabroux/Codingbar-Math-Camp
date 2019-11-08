#press A and B to choose a number

from microbit import *
import random

maxi = 50
mini = 1
answer = random.randint(mini+1, maxi-1)
guess = mini + 1

#main
display.scroll(str(mini) +' to '+ str(maxi), delay=50)
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(guess)
        if guess == answer:
            display.scroll('You Win!', delay=100)
            break
        elif guess > answer:
            maxi = guess
            guess = maxi - 1
            display.scroll(str(mini) +' to '+ str(maxi), delay=50)
        elif guess < answer:
            mini = guess
            guess = mini + 1
            display.scroll(str(mini) +' to '+ str(maxi), delay=50)
       
    elif button_a.is_pressed():
        if guess == mini+1:
            display.scroll(guess, delay=50)
        else:
            guess -= 1
            display.scroll(guess, delay=50)
    elif button_b.is_pressed():
        if guess == maxi-1:
            display.scroll(guess, delay=50)
        else:
            guess += 1
            display.scroll(guess, delay=50)
