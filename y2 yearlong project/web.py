from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash ## Importing flask and other needed stuff
app = Flask(__name__)

@app.route("/home")#defining url
def index():
	return render_template('home.html')

@app.route("/aboutme")
def about():
	return render_template("aboutme.html")

@app.route("/contactme")
def contact():
	return render_template("contactme.html")

@app.route("/hello/", methods=['POST']) 
def hello():
	name = request.form['name'] 
	return render_template('hello.html', name=name)
if __name__ == "__main__": 
	app.debug = True 
	app.run() 
