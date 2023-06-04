from flask import Flask

app = Flash(__name__)

@app.route('/')
def hello_world():
	return 'Hello, Simple Flask application'
