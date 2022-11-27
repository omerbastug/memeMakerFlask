from flaskapp import app,db
from flask import render_template,request, jsonify, send_file
from flaskapp.Models.User import User

@app.route("/api/getmeme", methods=["GET"])
def get_meme():
    return send_file("..\\meme.png", mimetype='image/png')