from rest import app,db
from generateMeme import *
from flask import render_template,request, jsonify
from rest.Models.User import User

@app.route("/api/creatememe", methods=["POST"])
def create_meme():
    print(request.form)
    source = request.files.get("image").stream if request.files else request.form.get("image")
    isNet = isinstance(source,str)

    lower = request.form.get("lower") or ""
    upper = request.form.get("upper") or ""
    if upper + lower == "":
        return jsonify({"nope":"give me something"})

    try:
        generate_meme(source, net=isNet, top_text=upper,bottom_text=lower)
    except BaseException as err:
        print(err)
        return jsonify({"failed":"oops"})
    else:
        return jsonify({"success":"ok"})