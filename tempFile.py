from microbit import *

a = 0

display.clear()

while True:
    if accelerometer.is_gesture("shake"):
        a = 1
        
    if button_b.is_pressed():
        display.show(Image.HEART)
        sleep(500)
        display.clear()
        break
    
