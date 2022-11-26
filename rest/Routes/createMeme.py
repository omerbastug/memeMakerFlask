from rest import app,db
from generateMeme import *
from flask import render_template,request, jsonify, send_file
from rest.Models.User import User
from rest.Models.Meme import Meme

@app.route("/api/creatememe", methods=["POST"])
def create_meme():
    try: 
        body = request.form if request.content_type.startswith("multipart/form-data") else request.get_json()
        source = request.files.get("image").stream if request.files else body.get("image")
        lower = body.get("lower") or ""
        upper = body.get("upper") or ""
    except:
        return send_file("../error cat.png")

    
    if not source or upper + lower == "":
        return send_file("../error cat.png")

        
    meme = Meme(upper= upper, lower= lower, baseImageLink= source)
    pil_img =meme.draw() 

    if body.get("getLink") == "1":
        return jsonify({"src":meme.srcLink})
    else :
        img_io = BytesIO()
        
        pil_img.save(img_io, pil_img.format, quality=70)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/'+pil_img.format)

