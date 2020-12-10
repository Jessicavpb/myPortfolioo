from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)

@app.route("/") #default route => default page
def index():
	return "<h3>Hello Flask ...</h3>"

@app.route("/portfolio")
def portfolio():
	page = render_template("1.html")
	return page