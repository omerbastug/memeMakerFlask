from flaskapp import app
from flask import render_template, flash
from flask_login import current_user
@app.route("/creatememe" , methods=["get"])
def create_meme_page():
    if not current_user.is_authenticated:
        flash("Log in required", category='danger')
    return render_template("createMeme.html")