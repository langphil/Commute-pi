# Check public transport links arrival times
import requests, json
from config import *
from datetime import datetime


# TFL API URLs
tube_url = 'https://api.tfl.gov.uk/Line/piccadilly/Arrivals/' + tube_station + '/?direction=inbound&app_id=' + app_id + '&app_key=' + app_key
bus_url = 'https://api.tfl.gov.uk/Line/9/Arrivals?stopPointId=' + bus_stop + '&app_id=' + app_id + '&app_key=' + app_key
train_url = 'https://api.tfl.gov.uk/StopPoint/' + train_station +'/arrivals'
status_url = 'https://api.tfl.gov.uk/line/mode/tube/status'


# Check arrival time, including walk times for my commute to work (Bus, Tube, Train)
def commute(walk, mode, url):
    transport = requests.get(url).json()
    count = 0
    return transport
    for i in sorted(transport, key=lambda i: i['timeToStation']):
        if count <= 2:
            status = (i['timeToStation'] / 60 + walk)
            print mode + ' : leave in {} mins'.format(status)
            count += 1


# Check status of the Tube line
def status(url):
    transport = requests.get(url).json()
    status_desc = transport[8]['lineStatuses'][0]['statusSeverityDescription']

    if status_desc == "Good Service":
        print 'Piccadilly has a good service'
    else:
        print 'Get the bus'


# Show relevant transport based upon the current hour
def decision():
    now = datetime.now()
    hour = '%s' % (now.hour)

    if hour < 7 and hour > 9:
        status(status_url)
        commute(3, 'Train', train_url)
        commute(12, 'Tube', tube_url)

    else:
        commute(3, 'Train', train_url)
        commute(5, 'Bus', bus_url)

commute(3, 'Train', train_url)
decision()
