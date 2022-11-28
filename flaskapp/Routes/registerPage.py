from flaskapp import app
from generateMeme import *
from flask import render_template

@app.route("/register")
def register_meme_page():
    return render_template("registerPage.html")