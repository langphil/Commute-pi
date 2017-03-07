# Check Dart departure times for Bayside
import requests, json
from datetime import datetime
from xml.etree import ElementTree


# Call and parse XML file
url = 'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=Bayside'
response = requests.get(url)
train = ElementTree.fromstring(response.content)


# Looping and printing all Northside trains
def direction(final_stop):

    for x in train: # THIS GETS ME ALL THE PATIENT ATTRIBUTES
        origin = x[6].text
        destination = x[7].text
        location = x[11].text
        sched = x[17].text
        est = x[15].text
        dueIn = x[12].text

        if destination == final_stop:
            print 'Destination: ' + destination
            print 'Train is due in ' + dueIn + ' mins'
            print location
            print 'Scheduled: ' + sched
            print 'Estimated: ' + est
            print


direction('Bray')
direction('Howth')


# DEPRECATED CODE


# Parse XML
station = train[0][2].text
destination = train[0][7].text
nextTrainSched = train[0][17].text
nextTrainEst = train[0][15].text
justLeft = train[0][11].text


# Check whether the Dart will arrive at it's scheduled time
# Add a counter here to add up how late the Dart is
# Dart can be early
def onTime():
    if nextTrainEst == nextTrainSched:
        print 'Dart is on time'
    else:
        print 'Dart is not on time: originally scheduled for ' + nextTrainSched


#print 'The next Dart to ' + destination + ' leaves from ' + station + ' is at ' + nextTrainEst + '. It has just ' + justLeft + '.'
#onTime()
