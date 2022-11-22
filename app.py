from flask import Flask, render_template
from generateMeme import *
# from decouple import config
from flask_sqlalchemy import SQLAlchemy
import pymysql

import os
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
port = os.environ.get("DB_PORT")
database = os.environ.get("DB_NAME")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+password+'@'+host+':'+port+'/'+database
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    # url image
    url ="https://yt3.ggpht.com/ytc/AMLnZu-UjGeg336Ky8RoBC2hlRZ4vnlkVW3lTr0H0DOpVg=s900-c-k-c0x00ffffff-no-rj" 
    generate_meme(url, net=True, top_text="something",bottom_text="is up")
    # generate_meme("./images/greet.jpg", top_text="yoyoyoo",bottom_text="is up")
    return render_template("index.html",imgsrc="https://picsum.photos/200")