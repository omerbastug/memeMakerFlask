from flaskapp import app, mailjet
from flask import render_template, request, redirect, flash, url_for
from flaskapp.Models.User import User
from flaskapp.Models.GreetingMeme import GreetingMeme
from flask_login import login_user

@app.route("/register", methods=['GET'])
def register_meme_page():
    return render_template("registerPage.html")

def sendEmail(name,email,id):
    firstname = name.split()[0]
    greet = GreetingMeme( username= name, userId= id)
    greet.draw()
    src = greet.srcLink
    print(name,src,email)
    data = {
    'Messages': [
        {
        "From": {
            "Email": "bomersami@gmail.com",
            "Name": "Omer Sami"
        },
        "To": [
            {
            "Email": email,
            "Name": name
            }
        ],
        "Subject": "Account creatasdsdednew ",
        "TextPart": "My first Mailjet email",
        "TemplateLanguage": True,
        "TemplateID": 4398348,
        "Variables":{
            "name" : firstname,
            "src": src
            }
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

@app.route("/register", methods=['POST'])
def register_redirect():
    body = request.form
    try:
        newuser = User(fullName=body.get("fullname"),email=body.get("email"),password = body.get("password"))
        newuser.addToDB()
        login_user(newuser)
        flash("Account created.", category="success")
        sendEmail(name=newuser.fullName, email=newuser.email, id=newuser.id)
        # sendEmail(name=newuser.fullName, email= newuser.email, id=newuser.id)
        return redirect(url_for("index"))
    except BaseException as err:
        print(err)
        flash("oopsies", category='danger')
        return redirect(url_for("register_meme_page"))