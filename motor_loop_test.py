#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
 
def main(args):
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BCM)

    POWER_13_14 = 17
    PWM_7 = 27

    GPIO.setup(PWM_7, GPIO.OUT)
    pin = GPIO.PWM(PWM_7, 100) #100Hz
    pin.start(0)
    pin.ChangeDutyCycle(20)

    GPIO.setup(POWER_13_14, GPIO.OUT)
    GPIO.output(POWER_13_14,GPIO.HIGH)
    print("power on")
    time.sleep(5)
    print("power start")
    GPIO.output(POWER_13_14,GPIO.LOW)
    pin.ChangeDutyCycle(15)
    time.sleep(1)
    pin.ChangeDutyCycle(17)
    time.sleep(2)
    pin.ChangeDutyCycle(20)
    time.sleep(23)
    pin.ChangeDutyCycle(20)
    time.sleep(33)
    pin.ChangeDutyCycle(17)
    time.sleep(1)
    pin.ChangeDutyCycle(15)
    time.sleep(1)
    main(args)

if __name__ == "__main__":
    import sys
    main(sys.argv)

