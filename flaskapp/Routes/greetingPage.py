from flaskapp import app
from generateMeme import *
from flask import render_template

@app.route("/greeting")
def greeting_meme_page():
    return render_template("greetingMeme.html")