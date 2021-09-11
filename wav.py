#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import pygame
import pygame.mixer

class SOUND:
    def __init__(self):
        pygame.mixer.init()
        self.wav = pygame.mixer.Sound("heartbeat_low_enh.wav")
        return

    def play(self):
        #time.sleep(random.random()*0.02)
        self.wav.play()
        return

def main(args):
    s = SOUND()
    s.play()
    time.sleep(1)
    s.play()
    time.sleep(1)
    return

if __name__ == "__main__":
    import sys
    main(sys.argv)

