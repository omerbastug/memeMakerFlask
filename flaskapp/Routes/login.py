from flaskapp import app,db
from flask import jsonify, request
from flaskapp.Models.User import User
import bcrypt

@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json()
    try:
        user = User.query.filter_by(email=body['email']).first()
        if not user:
            return jsonify({"error":"user not found"}), 404
        bytepassword = body['password'].encode('utf-8')

        salt = user.salt.encode('utf-8')

        hash = bcrypt.hashpw(bytepassword, salt)

        userhash = user.hash.encode('utf-8')

        if hash != userhash:
            return jsonify({"error":"wrong password"}), 401
    except BaseException as err:
        print(err)
        return jsonify({"error":"?"}), 500
    respUser = user.as_dict()
    del respUser['hash']
    del respUser['salt']    
    return jsonify({"success":"logged in " + str(user.id), "user" : respUser})
