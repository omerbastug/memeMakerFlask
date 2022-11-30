from flaskapp import app, db
from flask import render_template, flash, request
from flaskapp.Models.Meme import Meme
from flaskapp.Models.TemplateCategory import TemplateCategory
from flask_login import current_user
@app.route("/browse")
def browse_memes_page():
    resp = db.session.execute("select srcLink from meme where memeid in (SELECT  max(memeId) FROM  meme join template_category tc on tc.templateLink = meme.baseImageLink where tc.categoryId = 2 GROUP BY userId) limit 10")
    
    return render_template("browseMemesPage.html",memes= resp)