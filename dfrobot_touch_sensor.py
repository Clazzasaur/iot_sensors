# DFROBOT TOUCH SENSOR V2
# GPIO 26 on the green connecetor. 3.3/5v on the red, gnd on black.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    state = GPIO.input(26)
    print(state)
    if state == False:
        print('Button Pressed')
        time.sleep(0.2)