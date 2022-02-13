from microbit import *

f = open('numbers.txt', 'w')

for i in range(10):
    f.write(str(accelerometer.get_x()))
    f.write('\n')
    sleep(200)
    
f.close()

"""
code to enter in the shell to retrieve logged data
>>> files = open("numbers.txt")
>>> content = files.read()
>>> print(content)

"""
