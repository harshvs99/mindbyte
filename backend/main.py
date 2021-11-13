# Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
# Main driver code for the project backend

from tables import *
import redis
import json
import uuid
from flask import Flask, Response, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import and_, desc
from helpers import getLoginToken, initativesDashboard

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    data = {"login": None, "token": None, "user_display_name": None, "errorMessage": None}
    enteredUsername = request.args.get('user')
    enteredPassword = request.args.get('password')
    if enteredUsername is None:
        return Response('Incomplete Info (Username missing)', 500)
    elif enteredPassword is None:
        return Response('Incomplete Info (Password missing)', 500)

    data = getLoginToken(enteredUsername, enteredPassword)
    print("data: ", data)
    if 'error' in data:
        return jsonify(data), 400

    return json.dumps(data)

@app.route('/dashboard', methods=['GET'])
@cross_origin()
def dashboard():
    data = {"login": None, "token": None, "user_display_name": None, "errorMessage": None}
    token = request.args.get('token')
    return jsonify(initativesDashboard(token))

if __name__ == "__main__":
    app.run(debug=True, port=6003)
