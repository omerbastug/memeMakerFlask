from flaskapp import app,db
from flask import jsonify, request
from flaskapp.Models.User import User

@app.route("/api/login", methods=["POST"])
def login():
    body = request.get_json()
    try:
        user = User.query.filter_by(email=body['email']).first()
        if not user:
            return jsonify({"error":"user not found"}), 404

        if not user.truePassword(body['password']):
            return jsonify({"error":"wrong password"}), 401

    except BaseException as err:
        print(err)
        return jsonify({"error":"?"}), 500
    respUser = user.as_dict()
    del respUser['hash']
    del respUser['salt']    
    return jsonify({"success":"logged in " + str(user.id), "user" : respUser})
