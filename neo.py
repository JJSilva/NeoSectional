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




#def setcolor(i, g, r, b):
#"""light up one pixel."""
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()
	print ('Press Ctrl-C to quit.')
	while True:
		index = sys.argv[1]
		args = sys.argv[2].split(',')
		color = Color(int(args[0]),int(args[1]),int(args[2]))

		print sys.argv
		print color
		
		strip.setPixelColor(index, 0,0,255)
		strip.show()
		time.sleep(1.0)


