#!/usr/bin/python
from flask import Flask,request
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

if __name__ == '__main__':
	app.run()