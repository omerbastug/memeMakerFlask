from rest import db
from generateMeme import *
from rest.Models.BaseModel import BaseModel
from io import BytesIO
import requests

from PIL import Image, ImageDraw, ImageFont

class Meme(db.Model,BaseModel):
    """This is the model of memes to be stored in the DB"""
    memeId = db.Column(db.Integer(), primary_key=True) # auto increment on default
    upper = db.Column(db.String(length = 200), nullable=True)
    lower = db.Column(db.String(length = 200), nullable=True)
    baseImageLink = db.Column(db.String(length = 200), nullable=False)
    srcLink = db.Column(db.String(length = 200), nullable=False, unique=True)
    userId = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    def __init__(self, **kwargs):
        super(Meme, self).__init__(**kwargs)

        if not self.baseImageLink:
            return

        # set PIL image
        if not isinstance(self.baseImageLink,str):
            # todo: upload to s3 and assign link
            self.image = Image.open(self.baseImageLink)
            self.baseImageLink = "link generated after s3 upload"
        else :
            response = requests.get(self.baseImageLink)
            source = BytesIO(response.content)
            self.image = Image.open(source)

    def draw(self):
        # todo: upload to s3 and save record to database
        return generate_meme(pilImage=self.image, top_text=self.upper, bottom_text=self.lower)