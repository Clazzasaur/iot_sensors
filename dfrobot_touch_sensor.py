# DFROBOT TOUCH SENSOR V2
# GPIO 26 on the green connecetor. 3.3/5v on the red, gnd on black.
# the PCB already has the appropriate resistors.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN) # setup as an input (we want to detect a HIGH)

while True:
    state = GPIO.input(26)
    if state == True: # so when a high is pressed...
        print('Surface pressed')
        time.sleep(0.2)
