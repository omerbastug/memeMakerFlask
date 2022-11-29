from flaskapp import db, s3client
from generateMeme import *
from flaskapp.Models.BaseModel import BaseModel
from flaskapp.Models.TemplateCategory import TemplateCategory
from io import BytesIO
import requests
import uuid

from PIL import Image, ImageDraw, ImageFont

class Meme(db.Model,BaseModel):
    """This is the model of memes to be stored in the DB"""
    memeId = db.Column(db.Integer(), primary_key=True) # auto increment on default
    upper = db.Column(db.String(length = 200), nullable=True)
    lower = db.Column(db.String(length = 200), nullable=True)
    baseImageLink = db.Column(db.String(length = 500), nullable=False)
    srcLink = db.Column(db.String(length = 500), nullable=False, unique=True)
    userId = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    def __init__(self, **kwargs):
        if kwargs.get("dontSave"):
            self.dontSave = True
            kwargs.__delitem__("dontSave")
        if kwargs.get("dontSaveTemplate"):
            self.dontSaveTemplate = True
            kwargs.__delitem__("dontSaveTemplate")
                
        super(Meme, self).__init__(**kwargs)

        if not self.baseImageLink:
            return

        # set PIL image
        if not isinstance(self.baseImageLink,str):
            self.image = Image.open(self.baseImageLink)

            # todo: upload to s3 and assign link
            img_io = BytesIO()
            self.image.save(img_io,format= self.image.format)
            img_io.seek(0)

            key = str(uuid.uuid4())
            s3client.put_object(
                Bucket="meme-maker-memes-flask",
                Body= img_io,
                Key= key,
                ContentType= "image/"+self.image.format,
                ACL= "public-read"
            )
            self.baseImageLink = '%s/%s' % ("https://meme-maker-memes-flask.s3.eu-central-1.amazonaws.com", key)
        else :
            response = requests.get(self.baseImageLink)
            source = BytesIO(response.content)
            self.image = Image.open(source)

        if not TemplateCategory.query.filter_by(templateLink= self.baseImageLink).first() and (not hasattr(self,"dontSaveTemplate") or self.dontSaveTemplate == None):
            template = TemplateCategory(templateLink= self.baseImageLink, categoryId=self.category if hasattr(self,"category") else 2)
            db.session.add(template)


    def draw(self):
        # todo: upload to s3 and save record to database
        img = generate_meme(pilImage=self.image, top_text=self.upper, bottom_text=self.lower)
        if hasattr(self,"dontSave"):
            return img

        img_io = BytesIO()
        img.save(img_io, img.format, quality=70)
        img_io.seek(0)

        key = str(uuid.uuid4())
        s3client.put_object(
            Bucket="meme-maker-memes-flask",
            Body= img_io,
            Key= key,
            ContentType= "image/"+img.format,
            ACL= "public-read"
        )
        self.srcLink = '%s/%s' % ("https://meme-maker-memes-flask.s3.eu-central-1.amazonaws.com", key)
        self.addToDB()
        return img