# Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
# Main driver code for the project backend
from flask import Flask
from tables import *
import redis
import json
import uuid
from flask import Flask, Response, jsonify, request
from flask_cors import CORS, cross_origin
from sqlalchemy import and_, desc
from helpers import getLoginToken, operationsProjects, operationsPeople

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    data = {"login": None, "token": None, "user_display_name": None, "errorMessage": None}
    enteredUsername = request.args.get('username')
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


@app.route('/operations', methods=['GET'])
@cross_origin()
def operations():
    # if not authenticateAPI(token):
    #     return {"error": "Not Authenticated"}
    choice = request.args.get('choice')
    if choice == "projects":
        return jsonify(operationsProjects("projects"))
    elif choice == "people":
        return jsonify(operationsPeople())
    elif choice == "pipeline":
        return jsonify(operationsProjects("pipeline"))
    else:
        return {"error": "Wrong Choice entered"}


if __name__ == "__main__":
    #app.run(debug=True, port=80)
    app.run(debug=True, port=6003)
