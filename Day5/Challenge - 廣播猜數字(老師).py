from microbit import *
import random, radio

def isValid(num):
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
    
answer = []
while len(answer) < 4:
    a = random.randint(1,9)
    if str(a) not in answer:
        answer.append(str(a))

radio.on()
display.scroll('on', loop=True, wait=False)
while True:
    incoming = radio.receive()
    if incoming:
        #cheat
        if incoming == '7777':
            display.show(answer)
            display.clear()
        elif isValid(incoming):
            checker_msg = checkAnswer(incoming, answer)[0]+'A'+checkAnswer(incoming, answer)[1]+'B'
            if checkAnswer(incoming, answer)[0] == '4':
                display.scroll('You win!', delay = 70)
                break
            else:
                display.scroll(incoming, delay=100)
                display.scroll(checker_msg, wait=False, loop=True, delay=100)
        else:
            display.scroll('wrong', delay = 100)