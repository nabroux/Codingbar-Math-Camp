#Due to memory issue, AI Mode's answer only has three number.
from microbit import *
from random import randint

answer = []

def generateAnswer():
    while len(answer) < 4:
        a = randint(1,9)
        if str(a) not in answer:
            answer.append(str(a))

def isValid(num):
    num = str(num)
    n1,n2,n3,n4 = num[0],num[1],num[2],num[3]
    if n1!=n2 and n1!=n3 and n2!=n3 and n3!=n4 and n2!=n4 and n1!=n4:
        return True
    else:
        return False

def checkAnswer(guess,ans):
    a_num = 0
    b_num = 0
    for i in range(4):
        if guess[i] in ans:
            b_num += 1
        if guess[i] == ans[i]:
            a_num += 1
            b_num -= 1
    return (str(a_num),str(b_num))
    
def playerGuess():
    player_guess = ''
    player_num = 9
    while len(player_guess) < 4:
        #cheat
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(answer)
            display.clear()
            
        elif button_a.is_pressed():
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
        
        if len(player_guess) == 4:
            if isValid(player_guess):
                return player_guess
            else:
                player_guess = ''
                display.scroll('X', delay=50)

#Game start! Player Mode.
generateAnswer()

while True:
    player_guess = playerGuess()
    checker_msg = checkAnswer(player_guess,answer)[0]+'A'+checkAnswer(player_guess,answer)[1]+'B'
    if checkAnswer(player_guess,answer)[0] == '4':
        display.scroll('You win!', delay = 70)
        break
    else:
        display.scroll(checker_msg, wait=False, loop=True, delay = 70)
