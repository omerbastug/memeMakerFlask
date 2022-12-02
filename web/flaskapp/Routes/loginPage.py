from flaskapp import app
from flaskapp.Models.User import User
from flask import render_template ,request, redirect, flash, url_for
from flask_login import login_user

@app.route("/login" , methods=['get'])
def login_meme_page():
    return render_template("loginPage.html")

@app.route("/login" , methods=['post'])
def login_redirect():
    body = request.form
    print(body)
    try:
        user = User.query.filter_by(email=body.get("email")).first()
        if not user:
            flash("User not found", category="danger")
            return redirect(url_for('login_meme_page'))

        if not user.truePassword(body.get('password')):
            flash("Incorrect password", category="danger")
            return redirect(url_for('login_meme_page'))

    except BaseException as err:
        print(err)
        flash("oopsie, server got bamboozled", category='danger')
        return redirect(url_for('login_meme_page'))

    login_user(user)
    flash("login successful", category='success')
    return redirect(url_for('index'))