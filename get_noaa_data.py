# Kyle Hart
# 04 Sept 2017
#
# Project: beastcode
# File: get_noaa_data.py
# Description: Uses NOAA's Climate Data Online web api togather and insert
# raw weather Data

from cdo_api_py import Client
import pandas as pd
from _datetime import datetime
import MySQLdb
from sqlalchemy import create_engine

def get_year_of_data(conn, client, station_list, year):

    startdate = datetime(year, 8, 1)
    enddate = datetime((year+1), 2, 1)

    # DataFrame to iterate through for stations
    frame = {'id': station_list}
    stations = pd.DataFrame(data=frame)

    # DataFrame for all results
    big_frame = pd.DataFrame()
    for rows, station in stations.iterrows():
        station_data = client.get_data_by_station(
            datasetid='GHCND',
            stationid=station['id'],
            startdate=startdate,
            enddate=enddate,
            return_dataframe=True
            # include_station_meta=True
        )
        columns = ['station', 'date', 'PRCP', 'SNOW']
        single = pd.DataFrame(station_data, columns=columns)
        big_frame = pd.concat([big_frame, single])
        # pprint(single)
    # Create a SqlAlchemy engine with the existing connection, then passed into pandas.to_sql
    db_engine = create_engine('mysql://', creator=conn)
    big_frame.to_sql(con=db_engine, name='raw_weather',if_exists='replace')
    conn.commit()

# Connect to DB
password = input("Please enter a password for DB: ")
conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd=password, db='league')
cursor = conn.cursor()

# Get list of stations
cursor.execute('SELECT DISTINCT station_id FROM team')
station_list = [ row[0] for row in cursor.fetchall()]

# Set params for API call
token = 'IwcNfdENuPAzCSYdQBXoxjkhqWiBxJpM'
client = Client(token, default_units='metric', default_limit=1000)

get_year_of_data(conn, client, station_list, 2008)


conn.close()





