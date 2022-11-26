from rest.Models.Meme import Meme
from rest import db
import requests
import os
from PIL import Image
from io import BytesIO
class GreetingMeme(Meme):
    def __init__(self, **kwargs):
        self.username = kwargs.get("username") or "anon"
        kwargs.__delitem__("username")
        print(kwargs)
        self.category = 1
        super(GreetingMeme, self).__init__(**kwargs)


    def draw(self):
        res = db.session.execute("SELECT tc.templateLink, mt.upper, mt.lower FROM template_category tc JOIN category c on tc.categoryId = c.categoryId JOIN meme_text mt on c.categoryId = mt.categoryId WHERE c.categoryName = 'greeting' ORDER BY RAND() LIMIT 1").first()
        # print(res)
        if not hasattr(self, 'image'):
            resp = requests.get(res[0])
            self.image = Image.open(BytesIO(resp.content))
        self.baseImageLink = res[0]
        self.upper=  res[1].format(self.username) if res[1] else ""
        self.lower = res[2].format(self.username) if res[2] else ""
        return super().draw()