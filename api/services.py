from flask import request, jsonify
from api import app
from functions import *

@app.route('/wind/about', methods=['GET','POST'])
def get_info():
	app.logger.info("Wind service API")
	return 'Wind service API'

@app.route('/wind/speed/point/<lat>/<lon>/<string:date>/<string:fc_time>', methods=['GET', 'POST'])
def get_speed(lat, lon, date, fc_time):
    speed = get_speed_at_point(date, fc_time, lat, lon)
    if speed is None:
        return jsonify ({"error": "not found"})
    return jsonify({"speed": speed})

@app.route('/wind/direction/point/<lat>/<lon>/<string:date>/<string:fc_time>', methods=['GET', 'POST'])
def get_direction(lat, lon, date, fc_time):
    dir = get_direction_at_point(date, fc_time, lat, lon)
    if dir is None:
        return jsonify ({"error": "not found"})
    return jsonify({"direction": dir})

@app.route('/tcdc/point/<lat>/<lon>/<string:date>/<string:fc_time>', methods=['GET', 'POST'])
def get_total_cloud_cover(lat, lon, date, fc_time):
    val = get_tcdc_at_point(date, fc_time, lat, lon)
    if val is None:
        return jsonify ({"error": "not found"})
    return jsonify({"tcdc": val})



