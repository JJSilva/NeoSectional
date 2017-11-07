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

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	print ('Press Ctrl-C to quit.')
	#while True:
	color = Color(int(args[0]),int(args[1]),int(args[2]))
	print sys.argv
	
	strip.begin()
while True:
		who1 = sys.argv[1].split(',')
		who2 = sys.argv[2].split(',')
		who3 = sys.argv[3].split(',')
		who4 = sys.argv[4].split(',')
		who5 = sys.argv[5].split(',')
		who6 = sys.argv[6].split(',')
		who7 = sys.argv[7].split(',')
		who8 = sys.argv[8].split(',')
		who9 = sys.argv[9].split(',')
		who10 = sys.argv[10].split(',')
		who11 = sys.argv[11].split(',')
		who12 = sys.argv[12].split(',')
		who13 = sys.argv[13].split(',')
		who14 = sys.argv[14].split(',')
		who15 = sys.argv[15].split(',')
		who16 = sys.argv[16].split(',')
		who17 = sys.argv[17].split(',')
		who18 = sys.argv[18].split(',')
		who19 = sys.argv[19].split(',')
		who20 = sys.argv[20].split(',')
		who21 = sys.argv[21].split(',')
		who22 = sys.argv[22].split(',')
		who23 = sys.argv[23].split(',')
		who24 = sys.argv[24].split(',')
		who25 = sys.argv[25].split(',')		
		who26 = sys.argv[26].split(',')
		who27 = sys.argv[27].split(',')
		who28 = sys.argv[28].split(',')
		who29 = sys.argv[29].split(',')
		who30 = sys.argv[30].split(',')
		who31 = sys.argv[31].split(',')
		who32 = sys.argv[32].split(',')
		who33 = sys.argv[33].split(',')
		who34 = sys.argv[34].split(',')
		who35 = sys.argv[35].split(',')
		who36 = sys.argv[36].split(',')
		who37 = sys.argv[37].split(',')
		who38 = sys.argv[38].split(',')
		who39 = sys.argv[39].split(',')
		who40 = sys.argv[40].split(',')
		who41 = sys.argv[41].split(',')
		who42 = sys.argv[42].split(',')
		who43 = sys.argv[43].split(',')
		who44 = sys.argv[44].split(',')
		who45 = sys.argv[45].split(',')
		who46 = sys.argv[46].split(',')
		who47 = sys.argv[47].split(',')
		who48 = sys.argv[48].split(',')
		who49 = sys.argv[49].split(',')
		who50 = sys.argv[50].split(',')

		neo1(strip, Color(int(who1[0]), int(who1[1]), int(who1[2])))
		neo2(strip, Color(int(who2[0]), int(who2[1]), int(who2[2])))
		neo3(strip, Color(int(who3[0]), int(who3[1]), int(who3[2])))
		neo4(strip, Color(int(who4[0]), int(who4[1]), int(who4[2])))
		neo5(strip, Color(int(who5[0]), int(who5[1]), int(who5[2])))
		neo6(strip, Color(int(who6[0]), int(who6[1]), int(who6[2])))
		neo7(strip, Color(int(who7[0]), int(who7[1]), int(who7[2])))
		neo8(strip, Color(int(who8[0]), int(who8[1]), int(who8[2])))
		neo9(strip, Color(int(who9[0]), int(who9[1]), int(who9[2])))
		neo10(strip, Color(int(who10[0]), int(who10[1]), int(who10[2])))
		neo11(strip, Color(int(who11[0]), int(who11[1]), int(who11[2])))
		neo12(strip, Color(int(who12[0]), int(who12[1]), int(who12[2])))
		neo13(strip, Color(int(who13[0]), int(who13[1]), int(who13[2])))
		neo14(strip, Color(int(who14[0]), int(who14[1]), int(who14[2])))
		neo15(strip, Color(int(who15[0]), int(who15[1]), int(who15[2])))
		neo16(strip, Color(int(who16[0]), int(who16[1]), int(who16[2])))
		neo17(strip, Color(int(who17[0]), int(who17[1]), int(who17[2])))
		neo18(strip, Color(int(who18[0]), int(who18[1]), int(who18[2])))
		neo19(strip, Color(int(who19[0]), int(who19[1]), int(who19[2])))
		neo20(strip, Color(int(who20[0]), int(who20[1]), int(who20[2])))
		neo21(strip, Color(int(who21[0]), int(who21[1]), int(who21[2])))
		neo22(strip, Color(int(who22[0]), int(who22[1]), int(who22[2])))
		neo23(strip, Color(int(who23[0]), int(who23[1]), int(who23[2])))
		neo24(strip, Color(int(who24[0]), int(who24[1]), int(who24[2])))
		neo25(strip, Color(int(who25[0]), int(who25[1]), int(who25[2])))
		neo26(strip, Color(int(who26[0]), int(who26[1]), int(who26[2])))
		neo27(strip, Color(int(who27[0]), int(who27[1]), int(who27[2])))
		neo28(strip, Color(int(who28[0]), int(who28[1]), int(who28[2])))
		neo29(strip, Color(int(who29[0]), int(who29[1]), int(who29[2])))
		neo30(strip, Color(int(who30[0]), int(who30[1]), int(who30[2])))
		neo31(strip, Color(int(who31[0]), int(who31[1]), int(who31[2])))
		neo32(strip, Color(int(who32[0]), int(who32[1]), int(who32[2])))
		neo33(strip, Color(int(who33[0]), int(who33[1]), int(who33[2])))
		neo34(strip, Color(int(who34[0]), int(who34[1]), int(who34[2])))
		neo35(strip, Color(int(who35[0]), int(who35[1]), int(who35[2])))
		neo36(strip, Color(int(who36[0]), int(who36[1]), int(who36[2])))
		neo37(strip, Color(int(who37[0]), int(who37[1]), int(who37[2])))
		neo38(strip, Color(int(who38[0]), int(who38[1]), int(who38[2])))
		neo39(strip, Color(int(who39[0]), int(who39[1]), int(who39[2])))
		neo40(strip, Color(int(who40[0]), int(who40[1]), int(who40[2])))
		neo41(strip, Color(int(who41[0]), int(who41[1]), int(who41[2])))
		neo42(strip, Color(int(who42[0]), int(who42[1]), int(who42[2])))
		neo43(strip, Color(int(who43[0]), int(who43[1]), int(who43[2])))
		neo44(strip, Color(int(who44[0]), int(who44[1]), int(who44[2])))
		neo45(strip, Color(int(who45[0]), int(who45[1]), int(who45[2])))
		neo46(strip, Color(int(who46[0]), int(who46[1]), int(who46[2])))
		neo47(strip, Color(int(who47[0]), int(who47[1]), int(who47[2])))
		neo48(strip, Color(int(who48[0]), int(who48[1]), int(who48[2])))
		neo49(strip, Color(int(who49[0]), int(who49[1]), int(who49[2])))
		neo50(strip, Color(int(who50[0]), int(who50[1]), int(who50[2])))
		




		#strip.setPixelColor(int(i),color)
		#strip.show()



