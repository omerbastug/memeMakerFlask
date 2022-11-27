from flaskapp import app
from generateMeme import *
from flask import render_template

@app.route("/creatememe" , methods=["get"])
def create_meme_page():
    return render_template("createMeme.html")