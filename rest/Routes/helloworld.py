from rest import app,db
from generateMeme import *
from flask import render_template
from rest.Models.User import User

@app.route("/")
def index():
    # url image
    # newusuer = User(fullName = "Omer Sami Bastug",email = "bomersami@gmail.com",hash = "pwhash", salt = "salttomysecret")
    # newusuer.addToDB()
    url ="https://yt3.ggpht.com/ytc/AMLnZu-UjGeg336Ky8RoBC2hlRZ4vnlkVW3lTr0H0DOpVg=s900-c-k-c0x00ffffff-no-rj" 
    generate_meme(url, net=True, top_text="welcome",bottom_text="i am glad youre here")
    # generate_meme("./images/greet.jpg", top_text="i got this",bottom_text="yurrr")
    return render_template("index.html",imgsrc="/api/getmeme")