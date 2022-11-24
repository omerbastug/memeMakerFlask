from rest import app,db
from flask import jsonify, request
from rest.Models.User import User
import bcrypt

@app.route("/api/register", methods=["POST"])
def register():
    body = request.get_json()

    bytepassword = body['password'].encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytepassword, salt)

    try:
        newuser = User(fullName=body['fullname'],email=body['email'],hash=hash,salt=salt)
        newuser.addToDB()
    except BaseException as err:
        print(err)
        return jsonify({"error":err})

    return jsonify({"success":"account created"})