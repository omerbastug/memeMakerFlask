from rest import app,db
from generateMeme import *
from flask import render_template
from rest.Models.User import User

@app.route("/")
def index():
    return render_template("index.html",imgsrc="/api/getmeme")