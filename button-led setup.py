import time
import board
import digitalio as dio
import random

btn1 = dio.DigitalInOut(board.D8)
btn1_direction = dio.Direction.INPUT

led1 = dio.DigitalInOut(board.D2)
led1.direction = dio.Direction.OUTPUT
led1.value = True

btn2 = dio.DigitalInOut(board.D9)
btn2_direction = dio.Direction.INPUT

led2 = dio.DigitalInOut(board.D3)
led2.direction = dio.Direction.OUTPUT
led2.value = True

btn3 = dio.DigitalInOut(board.D10)
btn3_direction = dio.Direction.INPUT

led3 = dio.DigitalInOut(board.D4)
led3.direction = dio.Direction.OUTPUT
led3.value = True

btn4 = dio.DigitalInOut(board.D11)
btn4_direction = dio.Direction.INPUT

led4 = dio.DigitalInOut(board.D5)
led4.direction = dio.Direction.OUTPUT
led4.value = True

while True:
    led1.value = btn1.value
    led2.value = btn2.value
    led3.value = btn3.value
    led4.value = btn4.value
    time.sleep(0.01)
