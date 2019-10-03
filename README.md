# Climate Analysis & Exploration


## Project Overview
The goal of this project was to review and analyze temperature and precipitation measurements across Hawaii.  The data was provided in a sqlite database.  I used sqlalchemy in python to connect to the database and query for data.

The goal of this project was to create a database shema and import data from the six .csv files provided of employee and department data.  Once created, a series of queries were preformed to analyze the employee data.


## Analysis Performed
The following queries were performed as part of the analysis:
* Precipitation Analysis 
    * Find last day of data available in database
    * Gather precipitation data for all locations for the last year of data in the database
    * Plot precipitation data
    * Perform summary stats on the precipitation data (mean, mode, avg, etc)
* Station Analysis
    * Find total number of stations with climate data
    * Find most active stations (stations with most measurements)
    * Gather temperature data for last years worth of measurements for stations
        Plot data in histogram
* Temperature Analysis I
    * Gather temperature data for all stations for the Months of June and December
    * Perform a paired T-test to see if the temperatures are similar for the months
* Temperature Analysis II
    * Gather temperature data between 2/20/2017 - 3/02/2017
    * Plot average temperature for time frame as a bar chart
        * Include standard error of max and min temps


## Flask API
With the initial analysis performed above, I created a Flask API that performs the following:
* Home page that displays available routes
* /api/v1.0/precipitation - returns dictionary of daily precipitation values for each station
* /api/v1.0/stations - returns list of all stations in database
* /api/v1.0/tobs - returns list of temperature observations for previous year available
* /api/v1.0/<start> - takes a start date as input and returns list of min, max and avg temperatures between start date and last date available in database
* /api/v1.0/<start>/<end> - takes a start and end date as input and returns a list of min, max and avg temperatues between dates provides


## Project Contents
* climate_analysis.ipynb - jupyter notebook file for analysis functions
* app.py - python file with FLASK api
* Resources - folder containing the data for project
* Images - images of charts created during anaylsis

