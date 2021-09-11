#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import wav
import RPi.GPIO as GPIO

LED1 = 13#4
LED2 = 19#6
LED3 = 6#13
LED4 = 5#19
LED5 = 26

LEDS = [LED1,LED2,LED3,LED4,LED5]

def led(mode):
    time.sleep(0.023)
    for i,j in enumerate(mode):
        if j:
            GPIO.output(LEDS[i],GPIO.HIGH)
    time.sleep(0.001)
    for i,j in enumerate(mode):
        if j:
            GPIO.output(LEDS[i],GPIO.LOW)

def main(args):
    GPIO.setwarnings(False)     
    GPIO.setmode(GPIO.BCM)
    
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

    POWER_13_14 = 17
    PWM_7 = 27

    INPUT1 = 2
    INPUT2 = 3
    #INPUT1 = INPUT2
    GPIO.setup(INPUT1,GPIO.IN)
    GPIO.setup(INPUT2,GPIO.IN)
    status = False

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
    time.sleep(1)
    pin.ChangeDutyCycle(18)
    startTime = time.time()

    modeSecEach = [8,8,8,8,8, 8,6,6,8,8, 8,4,4,4,8, 8]
    modeSec = []
    a = 0
    for i in modeSecEach:
        a += i
        modeSec.append(a)
    #modeSec = [1,3,5,7,9, 11,13,15,17,19, 21,23,25,27,29,31]
    modeList = [
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,1,0,0,0],
            [0,0,0,1,0],
            [1,0,0,0,0],

            [0,0,0,0,1],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,1,1,1,0],
            [1,1,1,1,1],

            [1,1,1,1,1],
            [0,1,1,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            ]
    modeIdx = 0
    mode = [0,0,0,0,0]
    check = True

    s = wav.SOUND()
    count = 0
    while(1):
        if GPIO.input(INPUT1):
            status = False
        else:
            if status == False:
                status = True
                check = True
                led(mode)
                count += 1
                if sum(mode) > 0:
                    #if count % (30/int(sum(mode)/2+1)) == 0:
                    if count % 30 == 0:
                        s.play()
        if check:
            checkTime = time.time() - startTime
            if checkTime >= modeSec[modeIdx]:
                if modeIdx == 0:
                    pin.ChangeDutyCycle(18)
                if modeIdx == 6:
                    pin.ChangeDutyCycle(20)
                if modeIdx == 7:
                    pin.ChangeDutyCycle(21)
                if modeIdx == 10:
                    pin.ChangeDutyCycle(20)
                if modeIdx == 11:
                    pin.ChangeDutyCycle(19)
                if modeIdx == 12:
                    pin.ChangeDutyCycle(18)
                if modeIdx == 13:
                    pin.ChangeDutyCycle(17)
                if modeIdx == 14:
                    pin.ChangeDutyCycle(16)
                if modeIdx == len(modeList):
                    break
                mode = modeList[modeIdx]
                modeIdx += 1
                print(mode)
                
    #pin.ChangeDutyCycle(17)
    #time.sleep(1)
    #pin.ChangeDutyCycle(15)
    #time.sleep(1)


if __name__ == "__main__":
    import sys
    main(sys.argv)

