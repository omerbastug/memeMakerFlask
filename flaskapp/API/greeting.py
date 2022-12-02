from flaskapp import app,db, limiter, sample_scope
from flask import jsonify, request, send_file, redirect
from flask_login import current_user
from flaskapp.Models.GreetingMeme import GreetingMeme
from io import BytesIO

@app.route("/api/greeting/get", methods=["GET"])
def greet_user():
    if not current_user.is_authenticated:
        return redirect("https://meme-maker-memes-flask.s3.eu-central-1.amazonaws.com/990d12be-d070-438d-b9b3-6849c08c84d4")
    link = None
    username = request.args.get("username", default=None, type=str)

    greet = GreetingMeme(baseImageLink= link, dontSaveTemplate= True, dontSave=True, username= username)
    image = greet.draw()

    img_io = BytesIO()
    image.save(img_io, image.format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/'+image.format)


@app.route("/api/greeting", methods=["POST"])
@limiter.limit("10 per day", key_func = lambda : current_user.id, exempt_when= lambda: current_user.is_authenticated and current_user.id == 1)
@limiter.limit("10/hour")
@sample_scope
def greet_user_post():
    if not current_user.is_authenticated:
        return jsonify({"src":"https://meme-maker-memes-flask.s3.eu-central-1.amazonaws.com/990d12be-d070-438d-b9b3-6849c08c84d4"})
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
    

    greet = GreetingMeme(baseImageLink= link, dontSaveTemplate= True, username= username, userId = current_user.id)
    image = greet.draw()

    if getLink:
        return jsonify({"src" : greet.srcLink})

    img_io = BytesIO()
    image.save(img_io, image.format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/'+image.format)
