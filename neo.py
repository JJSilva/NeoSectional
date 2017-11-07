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



def neo1(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(1, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo2(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(2, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo3(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(3, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo4(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(4, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo5(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(5, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo6(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(6, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo7(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(7, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo8(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(8, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo9(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(9, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo10(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(10, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo11(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(11, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo12(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(12, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo13(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(13, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo14(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(14, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo15(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(15, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo16(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(16, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo17(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(17, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo18(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(18, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo19(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(19, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo20(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(20, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo21(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(21, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo22(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(22, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo23(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(23, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo24(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(24, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo25(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(25, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo26(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(26, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo27(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(27, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo28(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(28, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo29(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(29, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo30(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(30, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo30(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(30, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo31(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(31, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo32(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(32, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo33(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(33, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo34(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(34, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo35(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(35, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo36(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(36, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo37(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(37, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo38(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(38, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo39(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(39, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo40(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(40, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo41(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(41, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo42(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(42, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo43(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(43, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo44(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(44, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def neo45(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(45, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo46(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(46, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo47(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(47, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo48(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(48, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo49(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(49, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def neo50(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(50, color)
	strip.show()
	time.sleep(wait_ms/1000.0)			

def neo(index, strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(int(index), color)
	strip.show()
	time.sleep(wait_ms/1000.0)		

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	print ('Press Ctrl-C to quit.')
	#while True:
	print sys.argv
	
	strip.begin()
	print ('Press Ctrl-C to quit.')

while True:
	count = int(sys.argv[1])
	print "count: " + str(count)	
	for x in range(0, int(count)):
		who = sys.argv[2].split(',')
		neo(x, strip, Color(int(who[0]), int(who[1]), int(who[2])))






		#strip.setPixelColor(int(i),color)
		#strip.show()



