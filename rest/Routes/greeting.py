from rest import app,db
from flask import jsonify, request, send_file
from rest.Models.GreetingMeme import GreetingMeme
from io import BytesIO

@app.route("/api/greeting/", methods=["POST"])
def greet_user():
    link = None
    username = None
    try:
        body = request.get_json()
        print(body)
        username = body.get("username")
        link = body.get("image") 
    except:
        pass
    greet = GreetingMeme(baseImageLink= link)
    image = greet.draw(username=username)
    img_io = BytesIO()
    image.save(img_io, image.format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/'+image.format)
