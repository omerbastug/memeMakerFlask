from flaskapp import app
from generateMeme import *
from flask import render_template

@app.route("/login")
def login_meme_page():
    return render_template("loginPage.html")