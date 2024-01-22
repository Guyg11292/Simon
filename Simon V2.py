import time
import board
import digitalio as dio
import random

btn1 = dio.DigitalInOut(board.D8)
btn1_direction = dio.Direction.INPUT

led1 = dio.DigitalInOut(board.D2)
led1.direction = dio.Direction.OUTPUT
led1.value = False

btn2 = dio.DigitalInOut(board.D9)
btn2_direction = dio.Direction.INPUT

led2 = dio.DigitalInOut(board.D3)
led2.direction = dio.Direction.OUTPUT
led2.value = False

btn3 = dio.DigitalInOut(board.D10)
btn3_direction = dio.Direction.INPUT

led3 = dio.DigitalInOut(board.D4)
led3.direction = dio.Direction.OUTPUT
led3.value = False

btn4 = dio.DigitalInOut(board.D11)
btn4_direction = dio.Direction.INPUT

led4 = dio.DigitalInOut(board.D5)
led4.direction = dio.Direction.OUTPUT
led4.value = False


def sequence():
    for x in list1:
        if x == 1:
            led1.value = True
            time.sleep(1)
            led1.value = False
        if x == 2:
            led2.value = True
            time.sleep(1)
            led2.value = False
        if x == 3:
            led3.value = True
            time.sleep(1)
            led3.value = False
        if x == 4:
            led4.value = True
            time.sleep(1)
            led4.value = False

    
    
def add(points):
    list1.append(random.choice(colors))
    points += 1
    print(points)
    return points


colors = (1,2,3,4)     
while True:
    list1 = [random.choice(colors)]
    points = 0
    print(list1)
    time.sleep(1)
    sequence()
    
    

