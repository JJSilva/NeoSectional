import urllib2
import xml.etree.ElementTree as ET
import time
from neopixel import *
import sys
import os


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
		

with open("airports") as f:
    airports = f.readlines()
airports = [x.strip() for x in airports]
print airports 

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()



url = "https://aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requestType=retrieve&format=xml&mostRecentForEachStation=constraint&hoursBeforeNow=1&stationString="

for airportcode in airports:
	print airportcode
	url = url + airportcode + ","

print url
content = urllib2.urlopen(url).read()
#print content
print content
metars = ET.fromstring(content)

i = 0

for airportcode in airports:
	airport = metars.find(".//" + airportcode).text
	print airport
	flightCateory = metars.findtext(".//" + airportcode).text
	color = Color(0,0,0)
	if flightCateory == "VFR":
		color = Color(255,0,0)
	elif flightCateory == "MVFR":
		color = Color(0,0,255)
	elif flightCateory == "IFR":
		color = Color(0,255,0)
	elif flightCateory == "LIFR":
		color = Color(0,128,128)
	print "Setting light " + airportcode + " " + str(i) + " " + flightCateory + " " + str(color)
	strip.setPixelColor(i, color)
	strip.show()
	i = i + 1






print "fin"












