#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
 
def main(args):
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BCM)
    LED1 = 13#4
    LED2 = 19#6
    LED3 = 5#13
    LED4 = 6#19
    LED5 = 26
    GPIO.setup(LED1,GPIO.OUT)
    GPIO.setup(LED2,GPIO.OUT)
    GPIO.setup(LED3,GPIO.OUT)
    GPIO.setup(LED4,GPIO.OUT)
    GPIO.setup(LED5,GPIO.OUT)
    GPIO.output(LED1,GPIO.LOW)
    GPIO.output(LED2,GPIO.LOW)
    GPIO.output(LED3,GPIO.LOW)
    GPIO.output(LED4,GPIO.LOW)
    GPIO.output(LED5,GPIO.LOW)
    GPIO.output(LED1,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED2,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED4,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED5,GPIO.HIGH)
    time.sleep(5)
            
if __name__ == "__main__":
    import sys
    main(sys.argv)

