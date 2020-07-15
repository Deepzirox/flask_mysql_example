from flask import Flask, request, render_template, redirect, url_for
from conexion import *
import json



app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def adduser():
	tup_db = startDataBase()
	name = request.form['nombre']
	insertUser(name, tup_db)
	return redirect("/", code=302)

@app.route('/usuarios', methods=['GET'])
def users():
	tup_db = startDataBase()
	return json.dumps(parseRows(getUsers(tup_db)))

if __name__ == '__main__':
	app.run(debug=True) 