from flaskapp import app,db
from flask import jsonify, request
from flaskapp.Models.User import User

@app.route("/api/register", methods=["POST"])
def register():
    body = request.get_json()
    try:
        newuser = User(fullName=body['fullname'],email=body['email'],password = body['password'])
        newuser.addToDB()
        respUser = newuser.as_dict()
        del respUser['hash']
        del respUser['salt']  
    except BaseException as err:
        print(err)
        return jsonify({"error":err}), 400

    return jsonify({"success":"account created", "user" : respUser}) , 201
