from microbit import *
index = 0
images = [Image.SILLY, Image.PACMAN, Image.TSHIRT, Image.UMBRELLA]
images_l = len(images)

while True:
    if button_a.was_pressed():
        if index == 0:
            index = images_l - 1
        else:
            index -= 1
        display.show(images[index], delay=50)
    if button_b.was_pressed():
        if index == images_l - 1:
            index = 0
        else:
            index += 1
        display.show(images[index], delay=50)
