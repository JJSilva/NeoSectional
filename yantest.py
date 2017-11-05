# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
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



# Define functions which animate LEDs in various ways. 
				
				
def yanon(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(1, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon2(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(2, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon3(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(3, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon4(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(4, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon5(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(5, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon6(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(6, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon7(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(7, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon8(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(8, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon9(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(9, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon10(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(10, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon11(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(11, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon12(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(12, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon13(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(13, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon14(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(14, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon15(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(15, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon16(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(16, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon17(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(17, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon18(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(18, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon19(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(19, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon20(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(20, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon21(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(21, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon22(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(22, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon23(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(23, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon24(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(24, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon25(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(25, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon26(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(26, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon27(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(27, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon28(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(28, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon29(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(29, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon30(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(30, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon30(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(30, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon31(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(31, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon32(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(32, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon33(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(33, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon34(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(34, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon35(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(35, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon36(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(36, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon37(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(37, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon38(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(38, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon39(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(39, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon40(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(40, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon41(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(41, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon42(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(42, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon43(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(43, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon44(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(44, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

def yanon45(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(45, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
def yanon46(strip, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(46, color)
	strip.show()
	time.sleep(wait_ms/1000.0)



		# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	print ('Press Ctrl-C to quit.')
	while True:
		who = sys.argv[1].split(',')
		yanon(strip, Color(int(who[0]), int(who[1]), int(who[2])))
		who2 = sys.argv[2].split(',')
		yanon2(strip, Color(int(who2[0]), int(who2[1]), int(who2[2])))
		who3 = sys.argv[3].split(',')
		yanon3(strip, Color(int(who3[0]), int(who3[1]), int(who3[2])))
		who4 = sys.argv[4].split(',')
		yanon4(strip, Color(int(who4[0]), int(who4[1]), int(who4[2])))
		who5 = sys.argv[5].split(',')
		yanon5(strip, Color(int(who5[0]), int(who5[1]), int(who5[2])))
		who6 = sys.argv[6].split(',')
		yanon6(strip, Color(int(who6[0]), int(who6[1]), int(who6[2])))
		who7 = sys.argv[7].split(',')
		yanon7(strip, Color(int(who7[0]), int(who7[1]), int(who7[2])))
		who8 = sys.argv[8].split(',')
		yanon8(strip, Color(int(who8[0]), int(who8[1]), int(who8[2])))
		who9 = sys.argv[9].split(',')
		yanon9(strip, Color(int(who9[0]), int(who9[1]), int(who9[2])))
		who10 = sys.argv[10].split(',')
		yanon10(strip, Color(int(who10[0]), int(who10[1]), int(who10[2])))
		who11 = sys.argv[11].split(',')
		yanon11(strip, Color(int(who11[0]), int(who11[1]), int(who11[2])))
		who12 = sys.argv[12].split(',')
		yanon12(strip, Color(int(who12[0]), int(who12[1]), int(who12[2])))
		who13 = sys.argv[13].split(',')
		yanon13(strip, Color(int(who13[0]), int(who13[1]), int(who13[2])))
		who14 = sys.argv[14].split(',')
		yanon14(strip, Color(int(who14[0]), int(who14[1]), int(who14[2])))
		who15 = sys.argv[15].split(',')
		yanon15(strip, Color(int(who15[0]), int(who15[1]), int(who15[2])))
		who16 = sys.argv[16].split(',')
		yanon16(strip, Color(int(who16[0]), int(who16[1]), int(who16[2])))
		who17 = sys.argv[17].split(',')
		yanon17(strip, Color(int(who17[0]), int(who17[1]), int(who17[2])))
		who18 = sys.argv[18].split(',')
		yanon18(strip, Color(int(who18[0]), int(who18[1]), int(who18[2])))
		who19 = sys.argv[19].split(',')
		yanon19(strip, Color(int(who19[0]), int(who19[1]), int(who19[2])))
		who20 = sys.argv[20].split(',')
		yanon20(strip, Color(int(who20[0]), int(who20[1]), int(who20[2])))
		who21 = sys.argv[21].split(',')
		yanon21(strip, Color(int(who21[0]), int(who21[1]), int(who21[2])))
		who22 = sys.argv[22].split(',')
		yanon22(strip, Color(int(who22[0]), int(who22[1]), int(who22[2])))
		who23 = sys.argv[23].split(',')
		yanon23(strip, Color(int(who23[0]), int(who23[1]), int(who23[2])))
		who24 = sys.argv[24].split(',')
		yanon24(strip, Color(int(who24[0]), int(who24[1]), int(who24[2])))
		who25 = sys.argv[25].split(',')
		yanon25(strip, Color(int(who25[0]), int(who25[1]), int(who25[2])))
		who26 = sys.argv[26].split(',')
		yanon26(strip, Color(int(who26[0]), int(who26[1]), int(who26[2])))
		who27 = sys.argv[27].split(',')
		yanon27(strip, Color(int(who27[0]), int(who27[1]), int(who27[2])))
		who28 = sys.argv[28].split(',')
		yanon28(strip, Color(int(who28[0]), int(who28[1]), int(who28[2])))
		who29 = sys.argv[29].split(',')
		yanon29(strip, Color(int(who29[0]), int(who29[1]), int(who29[2])))
		who30 = sys.argv[30].split(',')
		yanon30(strip, Color(int(who30[0]), int(who30[1]), int(who30[2])))
		who31 = sys.argv[31].split(',')
		yanon31(strip, Color(int(who31[0]), int(who31[1]), int(who31[2])))
		who32 = sys.argv[32].split(',')
		yanon32(strip, Color(int(who32[0]), int(who32[1]), int(who32[2])))
		who33 = sys.argv[33].split(',')
		yanon33(strip, Color(int(who33[0]), int(who33[1]), int(who33[2])))
		who34 = sys.argv[34].split(',')
		yanon34(strip, Color(int(who34[0]), int(who34[1]), int(who34[2])))
		who35 = sys.argv[35].split(',')
		yanon35(strip, Color(int(who35[0]), int(who35[1]), int(who35[2])))
		who36 = sys.argv[36].split(',')
		yanon36(strip, Color(int(who36[0]), int(who36[1]), int(who36[2])))
		who37 = sys.argv[37].split(',')
		yanon37(strip, Color(int(who37[0]), int(who37[1]), int(who37[2])))
		who38 = sys.argv[38].split(',')
		yanon38(strip, Color(int(who38[0]), int(who38[1]), int(who38[2])))
		who39 = sys.argv[39].split(',')
		yanon39(strip, Color(int(who39[0]), int(who39[1]), int(who39[2])))
		who40 = sys.argv[40].split(',')
		yanon40(strip, Color(int(who40[0]), int(who40[1]), int(who40[2])))
		who41 = sys.argv[41].split(',')
		yanon41(strip, Color(int(who41[0]), int(who41[1]), int(who41[2])))
		who42 = sys.argv[42].split(',')
		yanon42(strip, Color(int(who42[0]), int(who42[1]), int(who42[2])))
		who43 = sys.argv[43].split(',')
		yanon43(strip, Color(int(who43[0]), int(who43[1]), int(who43[2])))
		who44 = sys.argv[44].split(',')
		yanon44(strip, Color(int(who44[0]), int(who44[1]), int(who44[2])))
		who45 = sys.argv[45].split(',')
		yanon45(strip, Color(int(who45[0]), int(who45[1]), int(who45[2])))
		who46 = sys.argv[46].split(',')
		yanon46(strip, Color(int(who46[0]), int(who46[1]), int(who46[2])))
		
