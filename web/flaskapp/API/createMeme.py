from flaskapp import app, limiter, sample_scope
from flask import request, jsonify, send_file
from flaskapp.Models.User import User
from flaskapp.Models.Meme import Meme
from io import BytesIO
from flask_login import current_user

@app.route("/api/creatememe", methods=["POST"])
@limiter.limit("10 per day", key_func = lambda : current_user.id, exempt_when= lambda: current_user.is_authenticated and current_user.id == 1)
@limiter.limit("10/hour")
@sample_scope
def create_meme():
    if not current_user.is_authenticated:
        return jsonify({"src":"https://meme-maker-memes-flask.s3.eu-central-1.amazonaws.com/990d12be-d070-438d-b9b3-6849c08c84d4"})
    try: 
        body = request.form if request.content_type.startswith("multipart/form-data") else request.get_json()
        source = request.files.get("image").stream if request.files else body.get("image")
        lower = body.get("lower") or ""
        upper = body.get("upper") or ""
    except:
        return send_file("../error cat.png"), 500

    if not source or upper + lower == "":
        return send_file("../error cat.png"), 500

        
    meme = Meme(upper= upper, lower= lower, baseImageLink= source, userId=current_user.id)
    pil_img =meme.draw() 

    if body.get("getLink") == "1":
        return jsonify({"src":meme.srcLink})
    else :
        img_io = BytesIO()
        
        pil_img.save(img_io, pil_img.format, quality=70)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/'+pil_img.format)

