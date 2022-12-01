from flaskapp import app, db, limiter
from flask import send_file
from flaskapp.Models.Meme import Meme
from io import BytesIO
from flask_limiter.util import get_remote_address

@limiter.limit("10 per day", key_func = get_remote_address)
@app.route("/api/meme/random", methods=["get"])
def random_meme():
    # get 2 random rows from custom memes
    res = db.session.execute("SELECT baseImageLink,upper,lower from meme m join template_category tc on m.baseImageLink = tc.templateLink where tc.categoryId = 2 order by rand() limit 2")
    rows = [row for row in res]

    # get the base image from first row, prompt from second row
    link = rows[0][0]
    upper = rows[1][1]
    lower = rows[1][2]

    meme = Meme( baseImageLink = link, upper = upper , lower = lower, dontSave = True, dontSaveTemplate = True )
    img = meme.draw()
    buffer = BytesIO()
    img.save(buffer, format= img.format)
    buffer.seek(0)
    
    return send_file(buffer, mimetype="image/"+img.format)