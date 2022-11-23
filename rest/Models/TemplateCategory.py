from rest import db
from rest.Models.BaseModel import BaseModel

class TemplateCategory(db.Model,BaseModel):
    """Linking memes with categories"""
    templateLink = db.Column(db.String(length = 200), primary_key=True,nullable=False, unique=True)
    categoryId = db.Column(db.Integer(), db.ForeignKey("category.categoryId"), nullable=False)
