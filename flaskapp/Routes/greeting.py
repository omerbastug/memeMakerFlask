from flaskapp import app,db
from flask import jsonify, request, send_file
from flaskapp.Models.GreetingMeme import GreetingMeme
from io import BytesIO

@app.route("/api/greeting/", methods=["POST"])
def greet_user():
    link = None
    username = None
    getLink = False
    try: 
        body = request.form if request.content_type.startswith("multipart/form-data") else request.get_json()
        link = request.files.get("image").stream if request.files else body.get("image")
        if link == 'undefined':
            link = None
        username = body.get("username")
        getLink = body.get("getLink") == "1"
    except:
        pass
    

    greet = GreetingMeme(baseImageLink= link, dontSaveTemplate= True, username= username)
    image = greet.draw()

    if getLink:
        return jsonify({"src" : greet.srcLink})

    img_io = BytesIO()
    image.save(img_io, image.format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/'+image.format)
