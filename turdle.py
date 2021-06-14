from turtle import Turtle
from gpiozero import Button, MotionSensor
from time import sleep
ms = MotionSensor('BOARD16', queue_len = 3, threshold = .7)
up = Button('BOARD37')
down = Button('BOARD33')
left = Button('BOARD22')
right = Button('BOARD35')
turd1 = Turtle(shape = 'turtle')
while True:
    if up.is_pressed:
        turd1.forward(10)
    elif down.is_pressed:
        turd1.backward(10)
    elif left.is_pressed:
        turd1.right(45)
    elif right.is_pressed:
        turd1.right(45)
    if ms.motion_detected:
        turd1.clear()
    sleep(.2)