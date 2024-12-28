#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
 
def main(args):
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BCM)
    POWER = 22
    GPIO.setup(POWER,GPIO.OUT)
    while 1:
        GPIO.output(POWER,GPIO.LOW)
        print("LOW")
        time.sleep(1)
        GPIO.output(POWER,GPIO.HIGH)
        print("HIGH")
        time.sleep(1)

if __name__ == "__main__":
    import sys
    main(sys.argv)

