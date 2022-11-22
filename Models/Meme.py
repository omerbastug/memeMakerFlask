# from yoyo import db
from generateMeme import *
class Meme:
    """This is the model of memes to be stored in the DB"""
    
    def __init__(self,source,userid,upper,lower="") -> None:
        self.source = source
        self.userid = userid
        self.upper = upper
        self.lower = lower

    # to be implemented
    # def draw():
    #     generate_meme()