# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import random

from neopixel import *

# LED strip configuration:
LED_COUNT      = 200    # Number of LED pixels.
LED_PIN        = 18     # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000   #800000 DEFAULT - CHRIS CHANGED # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=25):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def dimCycle():
    for i in range(255):
        for j in range(LED_COUNT):
            strip.setPixelColor(j, Color(0,0,i))
        strip.show()
        time.sleep(.001)
    for i in range(255):
        for j in range(LED_COUNT):
            strip.setPixelColor(j, Color(0,0,255-i))
        strip.show()
        time.sleep(.001)

def dimDown(strip, pixelNum, wait):
    for i in range(255):
        strip.setPixelColor(pixelNum, Color(0,0,255-i))
        strip.show()
        time.sleep(wait)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def set_color(strip, color):
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
        strip.show()

def set_bright(brightness):
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()
    if 0 < brightness < 7:
        brightness = 7
    value = (int(brightness) * int(brightness) / 100)
    set_color(strip, Color(0,0,int(255*(value/100))))
    
def flicker(strip, color, color2, wait_ms=.000001):
        for j in range(256):
                for i in range(strip.numPixels()):
                        strip.setPixelColor(i, Color(0,0,0+j))
                strip.show()
                time.sleep(wait_ms/1000.0)

def off():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def twinkle():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()
    for i in range(120):
        third = list(range(0, strip.numPixels(),3))
        pixel = random.choice(third)
        pixel2 = random.choice(third)
        pixel3 = random.choice(third)
        strip.setPixelColor(pixel, Color(1,1,6))
        strip.setPixelColor(pixel2, Color(0,0,0))
        strip.show()
        time.sleep(.1)
        strip.setPixelColor(pixel2, Color(1,1,6))
        strip.setPixelColor(pixel3, Color(0,0,0))
        strip.show()
        time.sleep(.1)
        strip.setPixelColor(pixel3, Color(1,1,6))
        strip.setPixelColor(pixel, Color(0,0,0))
        strip.show()
        time.sleep(.1)


# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    try:
        while True:
            #twinkle()
            #dimCycle()
            off()
##            for i in range(3):
##                for i in range(abs(2-i), 200, 3):
##                    strip.setPixelColor(i, Color(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
##                for i in range(abs(1-i), 199, 3):
##                    strip.setPixelColor(i, Color(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
##                for i in range(abs(0-i), 198, 3):
##                    strip.setPixelColor(i, Color(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
##                strip.show()
##                time.sleep(.1)
                        ## Color wipe animations.
                        #colorWipe(strip, Color(255, 0, 0))  # Red wipe
                        #colorWipe(strip, Color(0, 255, 0))  # Blue wipe
                        #colorWipe(strip, Color(0, 0, 255))  # Green wipe
                        #set_color(strip, Color(0, 0, 10))
            #flicker(strip, Color(0,0,0), Color(0,0,255))
                        ## Theater chase animations.
                        #theaterChase(strip, Color(127, 127, 127))  # White theater chase
                        #theaterChase(strip, Color(127,   0,   0))  # Red theater chase
                        #theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
                        ## Rainbow animations.
                        #rainbow(strip)
                        #rainbowCycle(strip)
                        #theaterChaseRainbow(strip)
    except KeyboardInterrupt:
        off()
