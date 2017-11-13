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
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering
		



strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()


with open("/NeoSectional/airports") as f:
    airports = f.readlines()
airports = [x.strip() for x in airports]
print airports 


key = open('/NeoSectional/key', 'r').read().rstrip()


url = "https://api.checkwx.com/metar/"
for airportcode in airports:
	if airportcode == "NULL":
		continue
	print airportcode
	url = url + airportcode + ","

url = url[:-1]

url = url + "/decoded" 




print url

#opener.addheaders = headers

print key

req = urllib2.Request(url)

req.add_header('X-API-Key',key)
req.add_header('Accept', 'application/xml')
print req.headers



content = urllib2.urlopen(req).read()
print content


root = ET.fromstring(content)



mydict = {
	"":""
}


for metar in root.iter('metar'):
	if airportcode == "NULL":
		continue

	stationId = metar.find('icao').text
	flightCateory = metar.find('flight_category').text
	print stationId + " " + flightCateory
	if stationId in mydict:
		print "duplicate, only save first metar"	
	else:
		mydict[stationId] = flightCateory
	
	

print mydict

i = 0
for airportcode in airports:
	if airportcode == "NULL":
		i = i +1
		continue
	print 
	color = Color(0,0,0)

	flightCateory = mydict.get(airportcode,"No")
	print airportcode + " " + flightCateory

	if  flightCateory != "No":
		
		if flightCateory == "VFR":
			print "VFR"
			color = Color(255,0,0)
		elif flightCateory == "MVFR":
			color = Color(0,0,255)
			print "MVFR"
		elif flightCateory == "IFR":
			color = Color(0,255,0)
			print "IFR"
		elif flightCateory == "LIFR":
			color = Color(0,128,128)
			print "LIFR"
	else:
		color = Color(255,255,255)
		print "N/A"

	print "Setting light " + str(i) + " for " + airportcode + " " + flightCateory + " " + str(color)
	strip.setPixelColor(i, color)
	strip.show()
	
	i = i+1
print
print "fin"











