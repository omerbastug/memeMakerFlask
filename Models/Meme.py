from app import db
from generateMeme import *
class Meme(db.Model):
    """This is the model of memes to be stored in the DB"""
    memeId = db.Column(db.Integer(), primary_key=True) # auto increment on default
    upper = db.Column(db.String(length = 200), nullable=False)
    lower = db.Column(db.String(length = 200), nullable=True)
    baseImageLink = db.Column(db.String(length = 200), nullable=False)
    srcLink = db.Column(db.String(length = 200), nullable=False, unique=True)
    userId = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    # to be implemented
    # def draw():
    #     generate_meme()