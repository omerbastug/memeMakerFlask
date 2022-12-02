from flaskapp import app
from generateMeme import *
from flask import render_template

@app.route("/")
def index():
    return render_template("homepage.html", LoggedIn= False)
    # return render_template("index.html",imgsrc="/api/meme/random")