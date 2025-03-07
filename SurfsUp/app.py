# Import the dependencies.
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)
# Base.prepare(engine, reflect=True)

# reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Save references to each table
session = Session(engine)


# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data"""
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23").all()
    session.close()

    precip_dict = {date: prcp for date, prcp in results}
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    stations_list = list(map(lambda x: x[0], results))
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def temperature():
    """Return temperature observations for the most active station"""
    session = Session(engine)
    most_active_station = "USC00519281"
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= "2016-08-23").all()
    session.close()

    tobs_list = [{date: temp} for date, temp in results]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp_range(start, end=None):
    """Return min, avg, and max temp for given date range"""
    session = Session(engine)
    
    if not end:
        results = session.query(func.min(Measurement.tobs),
                                func.avg(Measurement.tobs),
                                func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    else:
        results = session.query(func.min(Measurement.tobs),
                                func.avg(Measurement.tobs),
                                func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

    temp_data = {"Min Temp": results[0][0], "Avg Temp": results[0][1], "Max Temp": results[0][2]}
    return jsonify(temp_data)

if __name__ == "__main__":
    app.run(debug=True)