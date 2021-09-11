#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
 
def main(args):
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BCM)
    INPUT1 = 2
    INPUT2 = 3
    #INPUT1 = INPUT2
    LED = 5
    GPIO.setup(INPUT1,GPIO.IN)
    GPIO.setup(INPUT2,GPIO.IN)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(0.3)
    status = False
    count = 0
    count2 = 0
    flashTime = 0.001
    while(1):
        if GPIO.input(INPUT1):
            status = False
        else:
            count2 += 1
            if count2 % 30 == 0:
                count += 1
            if status == False:
                status = True
                if count % 2 == 1:
                    flashTime = 0
                else:
                    flashTime = 0.0005 + count/2 * 0.0001
                time.sleep(0.018)
                GPIO.output(LED,GPIO.HIGH)
                time.sleep(flashTime)
                GPIO.output(LED,GPIO.LOW)
            
if __name__ == "__main__":
    import sys
    main(sys.argv)

