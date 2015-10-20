from api import app

@app.route('/wind/about', methods=['GET','POST'])
def get_info():
	app.logger.info("Wind service API")
	return 'Wind service API'

