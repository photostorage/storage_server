from bottle import Bottle, run, route, request, static_file
import os
import os.path
app = Bottle()

#@app.route('/testphoto')
@app.route('/updatephoto/<photoname>')
def update_photo(photoname):
	return "i will updata %s photos." % photoname
	
@app.post('/update/<name>')
def update(name):
	return static_file(name, "update/")

@app.route('/test1')
def test1():
	return 'test.'
	
#一个简单页面，可以用浏览器提交文件
#@app.route('/upload')
#def upload():
#	retusrn '"<html><head></head><body><form action "/upload" method="post" enctype="multipart/form-data"><input type="file" name="photofile" /><input type="submit" value="Upload" /></form></body></html>"'
#上传文件，本保存到本地		
@app.route('/upload', method = 'POST')
def do_upload():
	upload = request.files.get('photofile')
	name,ext = os.path.splitext(upload.filename) #split name and extern type
	new_name = 'new'+upload.filename
	upload.save(new_name, overwrite=True)
	return 'OK'

#获取文件
@app.route('/getphoto/<name>', method = 'GET')
def get_photo(name):
	return static_file(name, root='/home/zm/source/storage_server/server')

#查询某个文件是否存在
@app.route('/checkphoto/<name>', method = 'GET')
def check_photo(name):
	localname = '/home/zm/source/storage_server/server/' + name
	respose = 'check'
	try:
		fp = open(localname, 'r')
		if fp:
			fp.close()
	except :
		respose = respose + name + 'is not exist'
	else:
		respose = respose + name + 'is exist'
	finally:	
		return respose
		
run(app, host='localhost', port=8080, debug=True)
