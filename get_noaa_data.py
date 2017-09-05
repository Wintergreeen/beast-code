# Kyle Hart
# 04 Sept 2017
#
# Project: beastcode
# File: get_noaa_data.py
# Description: Uses NOAA's Climate Data Online web api togather and insert
# raw weather Data


import requests
import json
import pprint
from cdo_api_py import Client
import pandas as pd
from _datetime import datetime
from pprint import pprint


token = 'IwcNfdENuPAzCSYdQBXoxjkhqWiBxJpM'
client = Client(token, default_units='metric', default_limit=1000)
startdate = datetime(2008, 8, 1)
enddate = datetime(2009, 2, 1)
station_list = [
    'GHCND:US1MDAA0027',
    'GHCND:US1MDPG0041'
    ]
frame = { 'id': station_list }
stations = pd.DataFrame(data=frame)
for rows, station in stations.iterrows():
    station_data = client.get_data_by_station(
        datasetid = 'GHCND',
        stationid = station['id'],
        startdate = startdate,
        enddate = enddate,
        return_dataframe=True
        #include_station_meta=True
    )
    pprint(station_data)

'''
extent = {
"north": 39.14,
"south": 38.68,
"east": -76.65,
"west": -77.35,
}

stations = client.find_stations(
    datasetid = 'GHCND',
    extent=extent,
    startdate = startdate,
    enddate = enddate,
    return_dataframe=True,
    include_station_meta=True
)
'''
