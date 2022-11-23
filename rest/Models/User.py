from rest import db
from rest.Models.BaseModel import BaseModel
class User(db.Model,BaseModel):
    """User model"""

    id = db.Column(db.Integer(), primary_key=True) # auto increment on default
    fullName = db.Column(db.String(length = 30), nullable=False)
    email = db.Column(db.String(length = 200), nullable=False, unique=True)
    hash = db.Column(db.String(length=64), nullable=False)
    salt = db.Column(db.String(length=64), nullable=False)

    def addUser(self):
        db.session.add(self)
        db.session.commit()