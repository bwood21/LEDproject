# Direct port of the Arduino NeoPixel library
import time

from neopixel import *
from random import randint
import pywapi



# LED strip configuration:
LED_COUNT      = 32   # Number of LED pixels.
LED_PIN        = 18      # GPIO pin 
LED_FREQ_HZ    = 800000  # LED signal frequency 
LED_DMA        = 5       # DMA channel 
LED_BRIGHTNESS = 255     # Set 0 to 255
LED_INVERT     = False   # True to invert the signal 


# Define functions 
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
        for j in range(half): #temp
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
        

        for h in range(half,LED_COUNT):  #conditions
                if condition == "light rain":
                        strip.setPixelColor(h,Color(0,0,200))
                elif condition == "heavy t-storm":
                        strip.setPixelColor(h,Color(0,0,255))
                elif condition == "fair":
                        strip.setPixelColor(h,Color(255,255,0))
                elif condition == "cloudy":
                        strip.setPixelColor(h,Color(192,192,192))
                elif condition == "partly cloudy":
                        strip.setPixelColor(h,Color(192,192,192))
                elif condition == "mostly cloudy":
                        strip.setPixelColor(h,Color(192,192,192))
                elif condition == "snow":
                        strip.setPixelColor(h,Color(255,255,255))
                else:
                        strip.setPixelColor(h,Color(102,255,255))
        
        strip.show()
def colorClear(strip):
        for i in range(0,150):
                strip.setPixelColor(i,Color(0,0,0))
                strip.show()


# Main program
if __name__ == '__main__':
	# Create NeoPixel object
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library
	strip.begin()

	weatherLight(strip)
	print "Weather success"
	time.sleep(5)
	print "Preparing to poweroff"
	colorClear(strip)
	print "Program complete"
	

