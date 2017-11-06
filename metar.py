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
airportlist.append("kmry")
airportlist.append("ksns")
airportlist.append("kwvi")
airportlist.append("ke16")
airportlist.append("krhv")
airportlist.append("ksjc")
airportlist.append("knuq")
airportlist.append("kpao")
airportlist.append("ksql")
airportlist.append("khaf")
airportlist.append("khaf")
airportlist.append("ksfo")
airportlist.append("khwd")
airportlist.append("koak")
airportlist.append("klvk")
airportlist.append("kc83")
airportlist.append("ksba")
airportlist.append("koxr")
airportlist.append("kcma")
airportlist.append("kwhp")
airportlist.append("kvny")
airportlist.append("kbur")
airportlist.append("ksmd")
airportlist.append("klax")
airportlist.append("khhr")
airportlist.append("kemt")
airportlist.append("kpoc")
airportlist.append("kcno")
airportlist.append("kral")
airportlist.append("ktoa")
airportlist.append("klgb")
airportlist.append("kful")
airportlist.append("ksna")
airportlist.append("ksli")
airportlist.append("kf70")
airportlist.append("kl35")
airportlist.append("kpsp")
airportlist.append("ktrm")
airportlist.append("ksdm")
airportlist.append("ksee")
airportlist.append("kokb")
airportlist.append("kcrq")
airportlist.append("krnm")
airportlist.append("kmyf")
airportlist.append("krnm")
airportlist.append("ksan")
airportlist.append("kavx")





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


	print "Setting light " + str(i) + " to " + flightCateory + " " + color

	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()
	rgb = color.split(',')
	strip.setPixelColor(i, Color(int(rgb[0]), int(rgb[1]), int(rgb[2])))
	strip.show()
	time.sleep(1.0)
	i += 1

print "fin"










