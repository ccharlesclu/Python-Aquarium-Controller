import random
import time
import pygame
import threading
from neopixel import *

strip = Adafruit_NeoPixel(120, 18, 800000, 5, False, 255)
strip.begin()

def rain():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/ledtest/rainTest.mp3")
    pygame.mixer.music.play(2)

def storm():
    def twinkle():
        #third = list(range(0, strip.numPixels(),3))
        third = list(range(0, strip.numPixels()))
        for i in range(100):
            pixel = random.choice(third)
            pixel2 = random.choice(third)
            pixel3 = random.choice(third)
            strip.setPixelColor(pixel, Color(1,1,6))
            strip.show()
            time.sleep(.1)
            strip.setPixelColor(pixel2, Color(1,1,6))
            strip.setPixelColor(pixel, Color(0,0,0))
            strip.show()
            time.sleep(.1)
            strip.setPixelColor(pixel3, Color(1,1,6))
            strip.setPixelColor(pixel2, Color(0,0,0))
            strip.show()
            time.sleep(.1)
            strip.setPixelColor(pixel3, Color(0,0,0))
            strip.show()

    def dimDown(list, strip, start, wait):
        for i in range(start):
            for j in list:
                strip.setPixelColor(j, Color(0,0,start-i))
            strip.show()
            time.sleep(wait)
        for i in list:
            strip.setPixelColor(i, Color(0,0,0))
        strip.show()

    def neoOn(list, strip, blue):
        for i in list:
            strip.setPixelColor(i, Color(0,0,blue))
        strip.show()

    def neoOff(list, strip):
        for i in list:
            strip.setPixelColor(i, Color(0,0,0))
        strip.show()

    def crack():
        for i in range(1,3):
            first = list(range(1, strip.numPixels(), 3))
            neoOn(first, strip, 255)
            time.sleep(.1)
            neoOff(first, strip)
            time.sleep(.1)
            neoOn(first, strip, 255)
            time.sleep(.1)
            neoOff(first, strip)
            time.sleep(.1)
            for x in range(1,7):
                dimDown(first, strip, int((200 / (x+1) / (x+1))), 2.4 / (200 / (x+1) / (x+1)))
##                if x == 1:
##                    bright = 200
##                    wait = .05
##                if x == 2:
##                    bright = 50
##                    wait = .08
##                dimDown(first, strip, bright, wait)
            time.sleep(1.5)

    def roll():
        second = list(range(2, strip.numPixels(), 3))
        for i in range(1, 4):
            neoOn(second, strip, 5)
            time.sleep(.05)
            neoOff(second, strip)
            time.sleep(.05)
            neoOn(second, strip, 5)
            time.sleep(.05)
            neoOff(second, strip)
            time.sleep(.05)
            neoOn(second, strip, 5)
            time.sleep(.05)
            neoOff(second, strip)
            time.sleep(.1)
            for i in range(1, 5):
                dimDown(second, strip, 15, .15)
            time.sleep(.1)
##        for i in range(1, 3):
##            for i in range(1, 6):
##                dimDown(second, strip, 20, .15)
##            time.sleep(1)

    def draw():
        third = list(range(0, strip.numPixels(), 3))
        for i in range(1,4):
            for i in range(1,3):
                for i in range(1,3):
                    dimDown(third, strip, 10, .2)
                time.sleep(1)
            time.sleep(1)                    
    
    def stopMusic():
        time.sleep(32)
        pygame.mixer.music.stop()
    
    RAIN = threading.Thread(name='rain', target=rain)
    STOPMUSIC = threading.Thread(name='stopMusic', target=stopMusic)
    CRACK = threading.Thread(name='crack', target=crack)
    ROLL = threading.Thread(name='roll', target=roll)
    DRAW = threading.Thread(name='draw', target=draw)
    TWINKLE = threading.Thread(name='twinkle', target=twinkle)
    
    RAIN.start()
    STOPMUSIC.start()
    time.sleep(1)
    CRACK.start()
    ROLL.start()
    DRAW.start()
    TWINKLE.start()

    time.sleep(32)

if __name__ == '__main__':
    storm()
