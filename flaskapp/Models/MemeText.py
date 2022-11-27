from flaskapp import db
from flaskapp.Models.BaseModel import BaseModel

class MemeText(db.Model,BaseModel):
    """Linking memes with categories"""
    textId = db.Column(db.Integer(), primary_key=True) # auto increment on default
    upper = db.Column(db.String(length = 200), nullable=True)
    lower = db.Column(db.String(length = 200), nullable=True)    
    categoryId = db.Column(db.Integer(), db.ForeignKey("category.categoryId"), nullable=False)
    