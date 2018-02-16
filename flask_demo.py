#!/usr/bin/python
from flask import Flask,request, render_template
import dbconn
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET'])
def index():
	print(request.headers.get('User-Agent'))
	print(request.remote_addr)
	return "Hello World!"

@app.route('/bye', methods=['GET'])
def n():
	print(request.headers.get('User-Agent'))
	print(request.remote_addr)
	return "Bye!"

@app.route('/qwerty',methods=['GET'])
def q():
	return "<h1>Qwerty! :)</h1>"

@app.route('/<int:id>/', methods=['GET'])
def dbr(id):
	# print(request.headers.get('User-Agent'))
	# print(request.remote_addr)
	
	return dbconn.dbretrieve(id)

@app.route('/disqus_test/1', methods=['GET'])
def disqus_test():
	return render_template('test.html')

@app.route('/disqus_test/2', methods=['GET'])
def disqus_test_2():
	return render_template('test.html')

if __name__ == '__main__':
	app.run()