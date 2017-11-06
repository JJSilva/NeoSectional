import urllib2
import xml.etree.ElementTree as ET
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


url = "https://aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=1&stationString="



airportlist = []
airportlist.append("KLGB")
airportlist.append("KSNA")

for airportcode in airportlist:
	print airportcode
	url = url + airportcode + ","


print url
content = urllib2.urlopen(url).read()
print content


metars = ET.fromstring(content)


i = 0
color = "0,0,0"
for metar in metars.iter('flight_category'):
	flightCateory = metar.text

	if flightCateory == "VFR":
		color = "0,255,0"
	elif flightCateory == "MVFR":
		color = "255,0,255"
	elif flightCateory == "IFR":
		color = "255,0,0"
	else:
		color = "0,0,0"


	print "Setting light" + i + " to " + flightCateory + " " color

	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()
	strip.setPixelColor(i, color)
	strip.show()
	time.sleep(wait_ms/1000.0)
	i += 1










