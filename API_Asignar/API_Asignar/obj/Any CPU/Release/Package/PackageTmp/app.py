"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import geopandas as gpd
import matplotlib as plt
from shapely.geometry import shape, Point
from urllib import request
from flask import Flask, jsonify, request
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def inicio():
    return jsonify({'mensaje':'API Activa'})

@app.route('/asignar')
def asignar_supervisor():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    gdf = gpd.read_file("gestores_bdb\gestores_bdb.shp")
    print(gdf)
    punto  = Point(float(lon), float(lat))

    contador = 0
    ci = ""

    for geom in gdf['geometry']:
        polygon = shape(gdf['geometry'][contador])
        if polygon.contains(punto):
            ci = gdf['CI'][contador]
            return jsonify({'CI':ci})

        contador = contador +1;
    return jsonify({'CI':ci})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
