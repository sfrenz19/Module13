import setup
from setup import RPL
import time
x = 0
while x <= 5:
    start = time.time
    z = 7
    while z == 7:
        current = time.time
        length = current - start
        if length < 50:
            RPL.servoWrite(1,500)
            RPL.servoWrite(0,2500)
        elif length > 50 and length < 100:
            RPL.servoWrite(1,2500)
            RPL.servoWrite(0,500)
        else:
            z = 9
    x +=1
