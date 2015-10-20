from flask import request, jsonify
from api import app
from wind import get_speed_at_point

@app.route('/wind/about', methods=['GET','POST'])
def get_info():
	app.logger.info("Wind service API")
	return 'Wind service API'


@app.route('/wind/speed/point', methods=['GET', 'POST'])
def get_speed():
    data = request.get_json()

    date = data.get('date')
    fc_time = data.get('forecast_time')
    lat = float(data.get('lat'))
    lon = float(data.get('lon'))

    speed = get_speed_at_point(date, fc_time, lat, lon)
    return jsonify({"speed": speed})




