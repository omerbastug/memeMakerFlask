from flaskapp import app
from flask_login import current_user
from flask import render_template, flash

@app.route("/greeting")
def greeting_meme_page():
    if not current_user.is_authenticated:
        flash("Log in required", category='danger')
    return render_template("greetingMeme.html")