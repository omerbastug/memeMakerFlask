from flaskapp import app
from flask import render_template, flash, request
from flaskapp.Models.Meme import Meme
from flaskapp.Models.TemplateCategory import TemplateCategory
from flask_login import current_user
@app.route("/memes")
def my_memes_page():
    page = request.args.get("page",default=1,type=int)
    userid = request.args.get("user",default=None,type=int)
    page = 1 if page < 1 else page
    if not userid:
        if not current_user.is_authenticated:
            flash("Log in required", category='danger')
            return render_template("myMemes.html")
        userid = current_user.id
    try:
        usersMemes = Meme.query.join(TemplateCategory, Meme.baseImageLink == TemplateCategory.templateLink).add_columns(Meme.srcLink).filter(Meme.userId == userid).filter(TemplateCategory.categoryId == 2).order_by(Meme.memeId).limit(10).offset((page-1)*10).all()
    except:
        flash("not possible", category='danger')
        return render_template("myMemes.html") 
    if len(usersMemes) == 0:
        flash("wow so empty", category='info')
    return render_template("myMemes.html",memes= usersMemes)