from microbit import *
import random

pattern = [Image.DIAMOND,Image.SMILE,Image.HAPPY,Image.HEART_SMALL,Image.RABBIT,\
        Image.XMAS,Image.UMBRELLA,Image.SNAKE,Image.BUTTERFLY,Image.SILLY,Image.YES,\
        Image.CHESSBOARD,Image.MUSIC_CROTCHET,Image.HOUSE,Image.SKULL,Image.SWORD,\
        Image.ROLLERSKATE,Image.SURPRISED,Image.ASLEEP,Image.ANGRY,Image.ARROW_E]
p_list = []

answer = random.choice(pattern)
pattern.remove(answer)

for i in range(50):
    image = random.choice(pattern)
    p_list.append(image)
    
for i in range(50):
    if (i+1)%9 == 0:
        p_list[i] = answer

index = 0
display.scroll(index+1, delay=50)
display.show(p_list[index])

while True:
    if button_a.is_pressed():
        if index == 0:
            index = 49
        else:
            index -= 1
            
        display.scroll(index+1, delay=50)
        display.show(p_list[index])
            
    elif button_b.is_pressed():
        if index == 49:
            index = 0
        else:
            index += 1
        
        display.scroll(index+1, delay=50)
        display.show(p_list[index])
        
    elif pin0.is_touched():
        break
    
display.show(['3','2','1',answer], delay=1000, wait=True)
sleep(2000)
display.scroll('Right?')
