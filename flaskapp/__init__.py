from flask import Flask, render_template
from generateMeme import *
from decouple import config
from sqlalchemy.sql.expression import select, func
from flask_sqlalchemy import SQLAlchemy
import boto3

user = config("DB_USER")
password = config("DB_PASSWORD")
host = config("DB_HOST")
port = config("DB_PORT")
database = config("DB_NAME")
s3AccesID = config("S3_ACCESS_KEY_ID")
s3AccessSecret = config("S3_ACCESS_SECRET")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+':'+password+'@'+host+':'+port+'/'+database
db = SQLAlchemy(app)

s3client = boto3.client("s3",
    aws_access_key_id=s3AccesID,
    aws_secret_access_key=s3AccessSecret)

from flaskapp.Models import User,Category,TemplateCategory,Meme, MemeText

with app.app_context():
    db.create_all()


from flaskapp.Routes import createMeme, getTheLatestMeme, index, register, login, greeting, randomMeme