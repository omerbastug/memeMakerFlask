from flaskapp import db
from flaskapp.Models.BaseModel import BaseModel
import bcrypt
from flask_login import UserMixin
class User(db.Model,BaseModel,UserMixin):
    """User model"""

    id = db.Column(db.Integer(), primary_key=True) # auto increment on default
    fullName = db.Column(db.String(length = 30), nullable=False)
    email = db.Column(db.String(length = 200), nullable=False, unique=True)
    hash = db.Column(db.String(length=64), nullable=False)
    salt = db.Column(db.String(length=64), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plainpw):
        bytepassword = plainpw.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytepassword, salt)
        self.hash = hash
        self.salt = salt

    def truePassword(self, passwordToCheck):
        bytepassword = passwordToCheck.encode('utf-8')
        salt = self.salt.encode('utf-8')

        hash = bcrypt.hashpw(bytepassword, salt)

        userhash = self.hash.encode('utf-8')

        return hash == userhash

    def addUser(self):
        db.session.add(self)
        db.session.commit()