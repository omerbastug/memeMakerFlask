from rest import app,db
from flask import jsonify, request
from rest.Models.User import User
import bcrypt

@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json()
    try:
        user = User.query.filter_by(email=body['email']).first()
        if not user:
            return jsonify({"error":"user not found"})
        bytepassword = body['password'].encode('utf-8')

        salt = user.salt.encode('utf-8')

        hash = bcrypt.hashpw(bytepassword, salt)

        userhash = user.hash.encode('utf-8')

        if hash != userhash:
            return jsonify({"error":"wrong password"})
    except BaseException as err:
        print(err)
        return jsonify({"error":"?"})
        
    return jsonify({"success":"logged in " + str(user.id)})
