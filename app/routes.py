from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def hello():
    return render_template("base.html")
