# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *
from random import randint
import pywapi



# LED strip configuration:
LED_COUNT      = 32   # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def weatherLight(strip):
        weather = pywapi.get_weather_from_weather_com('USIN0707')  #purdue = USIN0707
        #http://www.colorhexa.com/ff0000-to-00ff00
        temp = weather['current_conditions']['temperature']
        condition = weather['current_conditions']['text'].lower()
        farhTemp = (float(temp) * 1.8) + 32
        print "West Lafayette: "
        print "    Condition: " + condition
        print "    Temperature: %.0f F" % (farhTemp)
        half = LED_COUNT/2
        for j in range(strip.numPixels()): #temp
                 if farhTemp  < -10:
                        strip.setPixelColor(j,Color(255,0,0))
                 elif farhTemp < 0:
                        strip.setPixelColor(j,Color(255,43,0))
                 elif farhTemp < 10:
                         strip.setPixelColor(j,Color(255,85,0))
                 elif farhTemp < 20:
                         strip.setPixelColor(j,Color(255,128,0))
                 elif farhTemp < 30:
                         strip.setPixelColor(j,Color(255,170,0))
                 elif farhTemp < 40:
                         strip.setPixelColor(j,Color(255,213,0))
                 elif farhTemp < 50:
                         strip.setPixelColor(j,Color(255,255,0))
                 elif farhTemp < 60:
                        strip.setPixelColor(j,Color(213,255,0))
                 elif farhTemp < 70:
                         strip.setPixelColor(j,Color(170,255,0))
                 elif farhTemp < 80:
                         strip.setPixelColor(j,Color(128,255,0))
                 elif farhTemp < 90:
                         strip.setPixelColor(j,Color(85,255,0))
                 elif farhTemp < 100:
                         strip.setPixelColor(j,Color(43,255,0))
                 else:
                         strip.setPixelColor(j,Color(0,255,0))
        strip.show()
      #  for h in range(half,LED_COUNT):  #conditions
        

def colorClear(strip):
        for i in range(0,150):
                strip.setPixelColor(i,Color(0,0,0))
                strip.show()

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def brandonPattern(strip): #passes random values to random led
        z = randint(0,150)
        y = z-1
        for h in range(y,z):
                a = randint(0,255)
                b = randint(0,255)
                c = randint(0,255)
                strip.setPixelColor(h,Color(a,b,c))
                strip.show()

def recursiveRecursion(strip,color,iterations=10): #4 layers of looping fun
        for j in range(iterations):
		for q in range(3):
                        for z in range(3):
                                for i in range(0, strip.numPixels(), 3):
                                	strip.setPixelColor(i+q+z, color)
                                strip.show()
                                time.sleep(wait_ms/1000.0)
                                for i in range(0, strip.numPixels(), 3):
                                	strip.setPixel
                                        lColor(i+q+z, 0)
                

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixel
				lColor(i+q, 0)

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


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	weatherLight(strip)
	print "Weather success"
	time.sleep(5)
	print "Preparing to poweroff"
	colorClear(strip)
	print "Program complete"
	

	# print ('Press Ctrl-C to quit.')
	# while True:
		# Color wipe animations.
		# brandonPattern(strip)
		#recursiveRecursion(strip,Color(256,256,256)
		#colorClear(strip, Color(0, 0, 0))  # Poweroff
		#colorWipe(strip, Color(255, 255, 255))  # powertesting
		# Theater chase animations.
		#theaterChase(strip, Color(127, 127, 127))  # White theater chase
		#theaterChase(strip, Color(127,   0,   0))  # Red theater chase
		#theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
		# Rainbow animations.
		#rainbow(strip)
		#rainbowCycle(strip)
		#theaterChaseRainbow(strip)
