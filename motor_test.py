from gpiozero import Motor
from time import sleep

left = Motor(forward=17, backward=18)
right = Motor(forward=22, backward=23)

left.forward()
right.forward()
sleep(2)
left.stop()
right.stop()
