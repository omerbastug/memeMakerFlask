from app import db

class Category(db.Model):
    """Categories for memes"""
    categoryId = db.Column(db.Integer(), primary_key=True) # auto increment on default
    categoryName = db.Column(db.String(length=20), nullable=False, unique=True)