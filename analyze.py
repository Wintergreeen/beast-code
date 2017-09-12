# Kyle Hart
# 11 Sept 2017
#
# Project: beastcode
# File: analyze.py
# Description: Uses aggregated NCAAF and weather data to make predictions on given games

import MySQLdb
import re
import numpy
from sklearn.neighbors import KNeighborsClassifier

def getMeanAbsError(predicted, actual):
    n = len(predicted)
    totalerr = 0
    for i in range(n):
        totalerr += abs(predicted[i]-actual[i])
    return (totalerr/n)

def printStats(array):
    data_mean = numpy.mean(array)
    data_median = numpy.median(array)
    data_stddev = numpy.std(array)
    data_min = numpy.amin(array)
    data_max = numpy.amax(array)
    print("##### DATA ON RUSH YDS PER GAME ####")
    print("Mean = {}".format(data_mean))
    print("Median = {}".format(data_median))
    print("Max = {}".format(data_max))
    print("Min = {}".format(data_min))
    print("Std Dev = {}".format(data_stddev))

if __name__ == "__main__":
    #Connect to database
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd="#########", db='league')
    curs = conn.cursor()
    print("Loading data... \n")
    # General Query
    query = 'SELECT ' \
	            'CAST(game_stats.rush AS SIGNED), ' \
                'IFNULL(game_data.rush_strength, 0), '\
                'IFNULL(game_data.pass_strength, 0), '\
                'IFNULL(game_data.opp_rush_weak, 0), '\
                'IFNULL(game_data.opp_pass_weak, 0), '\
                'IFNULL(game_data.precipitation, 0), '\
                'IFNULL(game_data.snow, 0) '\
                'FROM game_data '\
                'JOIN game_stats ON 1=1 '\
		            'AND game_data.team_id = game_stats.team_id '\
		            'AND game_data.game_date = game_stats.game_date '\
                'WHERE 1=1 '\
		            'AND YEAR(game_data.game_date) <= 2010'
    # Get Training Data
    curs.execute(query)
    train_raw = curs.fetchall()
    train_rush = [ row[0] for row in train_raw ]
    train_stats = [ row[1:8] for row in train_raw ]

    # Get Test Data
    query = re.sub('2010', '2012', query)
    curs.execute(query)
    test_raw = curs.fetchall()
    actual_rush = [ row[0] for row in test_raw ]
    test_stats = [ row[1:8] for row in test_raw ]
    print("Training the machine... \n")
    #Train data with classifier using k-nearest neighbors technique
    machine = KNeighborsClassifier( n_neighbors=5, weights='distance', algorithm='kd_tree', n_jobs=-1)
    machine.fit(train_stats, train_rush)
    # Predictions and error
    print("Making predictions...\n")
    predicted_rush = machine.predict(test_stats)

    printStats(actual_rush)
    error = getMeanAbsError(predicted_rush, actual_rush)
    print("Error of prediction is {} yards".format(error))
