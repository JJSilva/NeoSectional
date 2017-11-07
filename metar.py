import urllib2
import xml.etree.ElementTree as ET
import time
from neopixel import *
import sys
import os



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


total = 1
color = "0,0,0"

args = ""


for metar in metars.iter('flight_category'):
	flightCateory = metar.text
	if flightCateory == "VFR":
		color = "255,0,0"
	elif flightCateory == "MVFR":
		color = "0,0,255"
	elif flightCateory == "IFR":
		color = "0,255,0"
	elif flightCateory == "LIFR":
		color = "0,125,125"	
	else:
		color = "255,255,255"
	print "Setting light " + str(total) + " " + flightCateory + " " + color
	args = args + " " + color
	#print args
	total = total+1
script = "sudo python neo.py " + str(total) + " " + args
print script
os.system(script)	
print "fin"












