import urllib2
import time
from neopixel import *
import sys


# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering
			

def neo(strip, index, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(int(index), color)
	strip.show()
	#time.sleep(wait_ms/1000.0)		

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	print ('Press Ctrl-C to quit.')
	#while True:
	print sys.argv
	
	
	print ('Welcome, Press Ctrl-C to quit.')

	strip.begin()
	index = sys.argv[1]

	color = sys.argv[2].split(",")
	green = int(color[0])
	red = int(color[1])
	blue = int(color[2])
	#print "count: " + str(count)	
	neo(strip, index, Color(green,red,blue))	
