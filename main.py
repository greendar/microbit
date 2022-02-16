import time
import MBmethods as MB

for i in range(100):
    MB.printTime()
    MB.printAccelMag()
    MB.printAccel()
    MB.detectFreeFall()
    time.sleep_ms(100)
