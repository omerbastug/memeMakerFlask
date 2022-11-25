from rest.Models.Meme import Meme
from rest import db
import os
from PIL import Image
class GreetingMeme(Meme):

    def draw(self,username):
        res = db.session.execute("SELECT tc.templateLink, mt.upper, mt.lower FROM template_category tc JOIN category c on tc.categoryId = c.categoryId JOIN meme_text mt on c.categoryId = mt.categoryId WHERE c.categoryName = 'greeting' ORDER BY RAND() LIMIT 1").first()
        print(res)
        if not hasattr(self, 'image'):
            abs = os.path.abspath(__file__)
            path = abs + "\\..\\..\\..\\images\\"+res[0]
            self.image = Image.open(path)
        username = username or "anon"
        self.upper=  res[1].format(username) if res[1] else ""
        self.lower = res[2].format(username) if res[2] else ""
        return super().draw()