#imports
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Hawaii Temperuature API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-08-01 <em>(avg temps from start date provided (YYYY-mm-dd))</em><br/>"
        f"/api/v1.0/2017-06-01/2017-08-01 <em>(avg temps between start and end dates provided (YYYY-mm-dd))</em><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation values for each station for last year in database"""
    # results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-22').all()
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp) \
        .filter(Measurement.date >= '2016-08-22') \
        .order_by(Measurement.station).order_by(Measurement.date) \
        .all()

    session.close()

    # create dictionary of station with value as dictionary of dates and precip values
    stations = {}
    for station, date, prcp in results:
        if station not in stations:
            stations[station] = {}
        stations[station][date] = prcp

    return jsonify(stations)


@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Stations in database"""
    results = session.query(Station.name).order_by(Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    result_list = list(np.ravel(results))

    return jsonify(result_list)

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'Tobs' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation values for last year of most active station in database"""
    results = session.query(Measurement.date, Measurement.prcp) \
        .filter(Measurement.date >= '2016-08-22') \
        .filter(Measurement.station == 'USC00519281') \
        .all()

    session.close()

    # Convert list of tuples into normal list
    result_list = list(np.ravel(results))

    return jsonify(result_list)

@app.route("/api/v1.0/<start_date>")
def stats_from_start_date(start_date):
    print("Server received request for 'Stats from Start Date' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Stations in database"""
    results = session.query(func.min(Measurement.tobs).label('min_tobs'), \
        func.max(Measurement.tobs).label('max_tobs'), \
        func.avg(Measurement.tobs).label('avg_tobs')) \
        .filter(Measurement.date >= start_date) \
        .all()

    session.close()

    # Convert list of tuples into normal list
    result_list = list(np.ravel(results))

    return jsonify(result_list)    

@app.route("/api/v1.0/<start_date>/<end_date>")
def stats_between_dates(start_date, end_date):
    print("Server received request for 'Stats between Dates' page...")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Stations in database"""
    results = session.query(func.min(Measurement.tobs).label('min_tobs'), \
        func.max(Measurement.tobs).label('max_tobs'), \
        func.avg(Measurement.tobs).label('avg_tobs')) \
        .filter(Measurement.date >= start_date) \
        .filter(Measurement.date <= end_date) \
        .all()

    session.close()

    # Convert list of tuples into normal list
    result_list = list(np.ravel(results))

    return jsonify(result_list)    

if __name__ == "__main__":
    app.run(debug=True)
