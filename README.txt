# Kyle Hart
# 4 Sept 2017
#
# Project: beastcode
# File: README.txt


INSTRUCTIONS TO BUILD DATASET:
The following files must be executed in exact order

1. pull_stats.sh 
	- Downloads NCAAF schedules, game, and player stats into raw/ as csv files
	- raw directory must also include schools.csv (manually built file with school/noaa-station relation)
2. create_tables.sql 
	-Creates raw tables to load csv's
3. load_csv.sql 
	-Loads csv files into raw tables --not including raw_weather
4. populate_tables.sql 
	-Migrates data from raw tables into usefull tables in schema --not including weather
5. get_noaa_data.py 
	- Downloads NOAA data into raw_weather table (This takes awhile)
6. migrate_weather.sql
	- Migrates data from raw_weather to weather table

