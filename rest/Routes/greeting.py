from rest import app,db
from flask import jsonify, request, redirect
from rest.Models.Meme import Meme
from generateMeme import *
import os
@app.route("/api/greeting", methods=["POST"])
def greet_user():
    try:
        res = db.session.execute("SELECT tc.templateLink, mt.upper, mt.lower FROM template_category tc JOIN category c on tc.categoryId = c.categoryId JOIN meme_text mt on c.categoryId = mt.categoryId WHERE c.categoryName = 'greeting' ORDER BY RAND() LIMIT 1").first()
        print(res)
        abs = os.path.abspath(__file__)
        path = abs + "\\..\\..\\..\\images\\"+res[0]
        upper=  res[1].format("user") if res[1] else ""
        lower = res[2].format("user") if res[2] else ""
        generate_meme(imageBufferOrURL=path, top_text=upper, bottom_text=lower,net=False)
    except BaseException as err:
        return jsonify({"oops": err})
    return redirect("/api/getmeme")
