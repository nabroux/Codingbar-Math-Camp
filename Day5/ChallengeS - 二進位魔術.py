from microbit import *

test0 = '1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 '
test1 = '2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 '
test2 = '4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 '
test3 = '8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 '
test4 = '16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 '

answer = 0

#0
display.scroll('GO!', delay=100)
display.scroll(test0, loop=True, delay=80, wait=False)
while True:
    if button_a.is_pressed():
        answer += 1
        break
    elif button_b.is_pressed():
        break
display.scroll('Good!', delay=100)

#1
display.scroll(test1, loop=True, delay=80, wait=False)
while True:
    if button_a.is_pressed():
        answer += 2
        break
    elif button_b.is_pressed():
        break
display.scroll('Good!', delay=100)

#2
display.scroll(test2, loop=True, delay=80, wait=False)
while True:
    if button_a.is_pressed():
        answer += 4
        break
    elif button_b.is_pressed():
        break
display.scroll('Good!', delay=100)
    
#3
display.scroll(test3, loop=True, delay=80, wait=False)
while True:
    if button_a.is_pressed():
        answer += 8
        break
    elif button_b.is_pressed():
        break
display.scroll('Good!', delay=100)

#4
display.scroll(test4, loop=True, delay=80, wait=False)
while True:
    if button_a.is_pressed():
        answer += 16
        break
    elif button_b.is_pressed():
        break
display.scroll('Good!', delay=100)

display.show(Image.SILLY)
sleep(1000)
display.scroll(answer, loop=True)
