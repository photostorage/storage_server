from bottle import route, run

@route("/updatephoto")
def updatephoto():
	return "i will updata a photo!"

@route('/getphoto')
def getphoto():
	return "i will get a photo!"
		

run(host="localhost", port=8080, debug=True)
