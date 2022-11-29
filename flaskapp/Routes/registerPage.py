from flaskapp import app
from flask import render_template, request, redirect, flash, url_for
from flaskapp.Models.User import User
from flask_login import login_user

@app.route("/register", methods=['GET'])
def register_meme_page():
    return render_template("registerPage.html")


@app.route("/register", methods=['POST'])
def register_redirect():
    body = request.form
    try:
        newuser = User(fullName=body.get("fullname"),email=body.get("email"),password = body.get("password"))
        newuser.addToDB()
        login_user(newuser)
        flash("Account created.", category="success")
        return redirect(url_for("index"))
    except BaseException as err:
        flash("oopsies", category='danger')
        return redirect(url_for("register_meme_page"))