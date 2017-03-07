# Check Dart departure times for Bayside
# ToDo
# 1. Loop through and only return results for a certain direction
# 2. Subtract estimated time from current time to work out how many minutes until next train
# 3. Add in a function to consider walking time to the station
# 4. Weather for walking?
# 5. Add a counter to count how many times the train is early / late
# 6. Factor in a messge for trains not running - night time etc..
# 7. Fix late message to factor in Dart being early


import requests, json
from datetime import datetime
from xml.etree import ElementTree

# Call and parse XML file
url = 'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=Bayside'
response = requests.get(url)
train = ElementTree.fromstring(response.content)

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
