from microbit import *
display.show(Image.SAD)
while True:
    gesture = accelerometer.current_gesture()
    if gesture == 'face up':
        display.show(Image.HAPPY)
    elif gesture == 'face down':
        display.show(Image.SAD)
