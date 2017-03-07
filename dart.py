# Check Dart departure times for Bayside
import requests, json
from datetime import datetime
from xml.etree import ElementTree


# Call and parse XML file
url = 'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=Bayside'
response = requests.get(url)
train = ElementTree.fromstring(response.content)


# Looping and printing all trains stopping at Bayside going both directions
def direction(line):

    for x in train:
        destination = x[7].text
        dueIn = x[12].text
        location = x[11].text
        sched = x[17].text
        est = x[15].text
        direction = x[18].text

        if direction == line:
            print 'Destination: ' + destination
            print 'Due in ' + dueIn + ' mins'
            print location
            print 'Scheduled: ' + sched
            print 'Estimated: ' + est
            print


direction('Southbound')
direction('Northbound')
