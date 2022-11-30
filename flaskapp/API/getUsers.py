from flaskapp import app, db
from flask import jsonify, request
from flaskapp.Models.User import User

@app.route("/api/user", methods=['GET'])
def get_users():
    name = f"%{request.args.get('name', default='', type=str)}%"
    
    # at least 2 character long name
    if len(name) < 5:
        return jsonify( { "users": [ {"fullname": "nope", "email": "cant have that"} ] } )

    users = User.query.filter(User.fullName.like(name)).limit(10).all()
    resp = [{"id":u.id, "fullname":u.fullName, "email": u.email} for u in users]
    
    return jsonify({"users":resp})