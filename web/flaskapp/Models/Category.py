from flaskapp import db
from flaskapp.Models.BaseModel import BaseModel

class Category(db.Model,BaseModel):
    """Categories for memes"""
    categoryId = db.Column(db.Integer(), primary_key=True) # auto increment on default
    categoryName = db.Column(db.String(length=20), nullable=False, unique=True)