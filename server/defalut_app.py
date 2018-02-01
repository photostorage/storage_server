from bottle import Bottle, run

app = Bottle()

@app.route('/testphoto')
@app.route('/updatephoto')
def update_photo():
	return "i will updata photos."

run(app, host='localhost', port=8080, debug=True)
