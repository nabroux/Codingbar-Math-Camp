from microbit import *
import radio

player_guess = ''
player_num = 9

while len(player_guess) < 4:
    if button_a.is_pressed():
        if player_num == 1:
            player_num = 9
        else:
            player_num -= 1
        display.scroll(player_num, delay=50)
            
    elif button_b.is_pressed():
        if player_num == 9:
            player_num = 1
        else:
            player_num += 1
        display.scroll(player_num, delay=50)
        
    elif pin0.is_touched():
        player_guess += str(player_num)
        display.scroll(player_guess, delay=70)
    
radio.on()
radio.send(player_guess)