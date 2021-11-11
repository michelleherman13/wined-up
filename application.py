# dependencies
from dbstring import database, connect_string
# import file with our library of functions
import wine_data 
# mongodb database class with the same function signitures ( same functions)
# from BellyButtonMongo import BellyButtonMongo

from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################

data = wine_data

#################################################
# Flask Setup
#################################################
application = Flask(__name__)


#################################################
# Flask Routes
#################################################

@application.route("/")
def index():

    return render_template("index.html", data=data)

@application.route("/api/v1.0")
def show_apis():
    """List all available api routes."""
    return (
        f"<h4>Available Routes:</h4>"
        f'<a href="/api/v1.0/flavors">/api/v1.0/flavors</a><br/>'
        f'<a href="/api/v1.0/regions">/api/v1.0/regions</a><br/>'
        f'<a href="/api/v1.0/topwineries">/api/v1.0/topwineries</a><br/>'     
        f'<a href="/api/v1.0/wineinfo">/api/v1.0/wineinfo</a><br/>'
        f'<a href="/api/v1.0/filteredwine/all/all">/api/v1.0/filteredwine/all/all</a><br/></br>'   
        f'<a href="/"><h4>Back</h4></a><br/>'  
        
        
    )    

@application.route("/api/v1.0/topwineries")
def top_wineries():
    return jsonify(data.top_wineries())

@application.route("/api/v1.0/wineinfo")
def wine_info():
    return jsonify(data.wine_info())

@application.route("/api/v1.0/flavors")
def flavors():
    return jsonify(data.flavors())

@application.route("/api/v1.0/regions")
def regions():
    return jsonify(data.regions())

@application.route("/api/v1.0/winerydata")
def winery_data():
    return jsonify(data.winery_data())

@application.route("/api/v1.0/filteredwine/<flavor>/<region>")
def filtered_top_wine(flavor, region):
    return jsonify(data.filtered_top_wine(flavor, region))

if __name__ == '__main__':
    application.run(debug=True)
