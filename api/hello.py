from api import app
@app.route('/')
def hello_world():
	app.logger.debug('A value for debugging')
	return 'Hello World!'