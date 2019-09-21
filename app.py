#################################################
# Dependencies and Setup
#################################################

from flask import Flask, render_template, jsonify, request # Lori/Sergio: not sure if we need jsonify.
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import sqlite3

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
# Winter = Base.classes.winter_clean
# Summer = Base.classes.summer_clean
# Athlete = Base.classes.athlete_clean
# Regions = Base.classes.regions_clean
# Country = Base.classes.country_clean
# Soccer = Base.classes.soccer_clean

#################################################
# Route Setup
#################################################

# Route to render index.html template
@app.route("/")
def home():

    con = sqlite3.connect("./Resources/gdp_olympic.sqlite")
    cursor = con.cursor()
    cursor.execute("SELECT year FROM winter_clean")
    print(cursor.fetchall())
    
    return render_template("index.html")

# End the Flack doc with standard ending
if __name__ == "__main__":
    app.run(debug=False)