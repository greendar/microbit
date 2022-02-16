from microbit import *
import time

def printAccel():
    print(accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z())

def printAccelMag():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print((x**2 + y**2 + z**2)**0.5, end=" ")

def detectFreeFall():
    if accelerometer.is_gesture('freefall'):
        print("FreeFall")

def printTime():
    print(time.ticks_us(), end=": ")
