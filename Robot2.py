import setup
from setup import RPL
rightsensor = 23
rightmotor = 0
leftmotor = 1
while True:
  if RPL.readDistance(rightsensor) < 70000:
    RPL.servoWrite(rightmotor,2000)
  else:
    RPL.servoWrite(rightmotor,0)
 
