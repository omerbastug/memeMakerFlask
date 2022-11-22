from flask import Flask, render_template
from generateMeme import *
from decouple import config
from flask_sqlalchemy import SQLAlchemy
 
import os
user = config("DB_USER")
password = config("DB_PASSWORD")
host = config("DB_HOST")
port = config("DB_PORT")
database = config("DB_NAME")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+':'+password+'@'+host+':'+port+'/'+database
db = SQLAlchemy(app)

from Models.User import User
from Models.Category import Category
from Models.TemplateCategory import TemplateCategory
from Models.Meme import Meme

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    # url image
    url ="https://yt3.ggpht.com/ytc/AMLnZu-UjGeg336Ky8RoBC2hlRZ4vnlkVW3lTr0H0DOpVg=s900-c-k-c0x00ffffff-no-rj" 
    generate_meme(url, net=True, top_text="something",bottom_text="is up")
    # generate_meme("./images/greet.jpg", top_text="yoyoyoo",bottom_text="is up")
    return render_template("index.html",imgsrc="https://picsum.photos/200")