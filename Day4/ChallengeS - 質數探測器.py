from microbit import *

number = 1000
count = 0
prime=[]

for i in range(2,number):
    for n in range(2,i):
        if i%n==0:
            count += 1
    if count == 0:
        prime.append(i)
    count=0

index = 0
display.scroll(prime[index], delay=100)

while True:
    if button_a.is_pressed():
        index += 1
        display.scroll(prime[index], delay=100)

        
