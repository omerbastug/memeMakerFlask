from flaskapp import app
from generateMeme import *
from flask import render_template

@app.route("/random")
def random_meme_page():
    return render_template("index.html",imgsrc="/api/meme/random")