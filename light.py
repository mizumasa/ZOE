#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
 
def main(args):
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BCM)
    INPUT1 = 2
    INPUT2 = 3
    if len(args) > 1:
        print("INPUT 2")
        INPUT1 = INPUT2
    else:
        print("INPUT 1")
    LED = 4
    GPIO.setup(INPUT1,GPIO.IN)
    GPIO.setup(INPUT2,GPIO.IN)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(0.3)
    status = False
    while(1):
        if GPIO.input(INPUT1):
            status = False
        else:
            if status == False:
                print(1)
                status = True
                time.sleep(0.018)
                GPIO.output(LED,GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(LED,GPIO.LOW)
            
if __name__ == "__main__":
    import sys
    main(sys.argv)

