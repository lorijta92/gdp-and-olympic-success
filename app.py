#################################################
# Dependencies and Setup
#################################################
import os

import pandas as pd
import numpy

from flask import Flask, render_template, jsonify, request # Lori/Sergio: not sure if we need jsonify.
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Create an instance of Flask
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# Configure our Flask instance to sqllite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Resources/gdp_olympic.sqlite'

# Create database object using SQLAlchemy
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Winter = Base.classes.winter
Summer = Base.classes.summer
Athlete = Base.classes.athlete
Regions = Base.classes.regions
Country = Base.classes.country
Soccer = Base.classes.soccer

#################################################
# Route Setup
#################################################

# Route to render index.html template
@app.route("/")
def home():

    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Winter).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(df)
    return render_template("index.html")

# End the Flack doc with standard ending
if __name__ == "__main__":
    app.run()