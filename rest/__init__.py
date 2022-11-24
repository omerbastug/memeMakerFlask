from flask import Flask, render_template
from generateMeme import *
from decouple import config
from sqlalchemy.sql.expression import select, func
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

from rest.Models import User,Category,TemplateCategory,Meme, MemeText

with app.app_context():
    db.create_all()
    # res = db.engine.execute("SELECT * FROM user ORDER BY RAND() limit 1")
    # for item in res:
    #     print(item.id)


from rest.Routes import helloworld, createMeme, getTheLatestMeme, register, login, greeting