from api import app

@app.route('/wind/info', methods=['GET','POST'])
def get_info():
	app.logger.info("get wind info")
	return 'Wind info'
