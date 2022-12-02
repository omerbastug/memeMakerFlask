from flaskapp import app
from flask import send_file

@app.route("/favicon.ico", methods=['GET'])
def favicon():
    return send_file("../images/favicon.ico")