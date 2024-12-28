#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import random
import pygame
import pygame.mixer

class SOUND:
    def __init__(self):
        pygame.mixer.init()
        self.wav = pygame.mixer.Sound("heartbeat_low_enh.wav")
        self.count = pygame.mixer.Sound("count.wav")
        return

    def play(self):
        #time.sleep(random.random()*0.02)
        self.wav.play()
        return
    def playCount(self):
        self.count.play()
        return

class SOUND2:
    def __init__(self):
        return

    def play(self):
        os.system("sudo -u pi aplay /home/pi/ZOE/heartbeat_low_enh.wav &")
        return
    def playCount(self):
        os.system("sudo -u pi aplay /home/pi/ZOE/count.wav &")
        return


def main(args):
    s = SOUND2()
    s.play()
    time.sleep(1)
    s.playCount()
    time.sleep(1)
    return

if __name__ == "__main__":
    import sys
    main(sys.argv)

