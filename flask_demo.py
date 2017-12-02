#!/usr/bin/python
from flask import Flask,request

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
	