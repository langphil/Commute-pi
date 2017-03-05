# Creating functions that check public transport links for my commute to work.
import requests, json
from config import *
from datetime import datetime


# TFL API URLs
tube_url = 'https://api.tfl.gov.uk/Line/piccadilly/Arrivals/' + tube_station + '/?direction=inbound&app_id=' + app_id + '&app_key=' + app_key
bus_url = 'https://api.tfl.gov.uk/Line/9/Arrivals?stopPointId=' + bus_stop + '&app_id=' + app_id + '&app_key=' + app_key
train_url = 'https://api.tfl.gov.uk/StopPoint/' + train_station +'/arrivals'


# Function that checks arrival time, including walk times for my commute to work
# Feeds arguments for walk time to station, mode of transport (Tube, Train, Bus) and the URl for the API feed
def commute(walk, mode, station):
    url = station
    transport = requests.get(url).json()
    count = 0

    for i in sorted(transport, key=lambda i: i['timeToStation']):
        if count <= 2:
            status = (i['timeToStation'] / 60 + walk)
            print mode + ' : leave in {} mins'.format(status)
            count += 1


# A function that will show relevant transport based upon the current hour
def decision():
    now = datetime.now()
    hour = '%s' % (now.hour)

    if hour < 7 or hour > 9:
        commute(3, 'Train', train_url)
        commute(5, 'Bus', bus_url)

    else:
        commute(12, 'Tube', tube_url)
        commute(5, 'Bus', bus_url)


decision()
