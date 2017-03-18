import math
import scrollphat
import time
import sys
import requests
import json
from datetime import datetime
from xml.etree import ElementTree


# Setting up Scrollphat
scrollphat.set_brightness(3)
scrollphat.set_rotate(True)
scrollphat.update()


# Parsing API data to filter out trains going to the Southside
def direction(line):
    scrollphat.clear_buffer()
    timeUntil = 0

    # Calling Dart API
    url = 'http://api.irishrail.ie/realtime/realtime.asmx/' \
          'getStationDataByNameXML?StationDesc=Bayside'
    response = requests.get(url)
    train = ElementTree.fromstring(response.content)

    for x in train:
        direction = x[18].text
        timeUntil = float(x[12].text)

        if direction == line:
            scrollphat.write_string("%.0f" % timeUntil)
            time.sleep(5)
    scrollphat.update()
    time.sleep(1)


while True:
    direction('Southbound')
