# Add your Python code here. E.g.
from microbit import *

for i in range(2,10):
    for j in range(1,10):
        display.scroll(str(i)+'*'+str(j)+'='+str(i*j), delay=100)
