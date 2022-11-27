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
        body = request.get_json()
        username = body.get("username")
        link = body.get("image")

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
