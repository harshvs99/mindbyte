# Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
# Helper code snippets, for each function

from tables import *
import datetime as dt
import uuid
from flask.globals import session
import redis

session = Session()

loginTokens = {}
cacheTokens = redis.Redis()


def getLoginToken(enteredUsername, enteredPassword):
    try:
        data = {"login": None, "token": None, "user_display_name": None, "errorMessage": None}
        loginCredentials = {}
        users = session.query(User).all()
        for user in users:
            loginCredentials[user.username] = user.password

        print("LoginCreds so far: ", loginCredentials)
        if enteredUsername in loginCredentials:
            if loginCredentials[enteredUsername] == enteredPassword:
                data['login'] = "authenticated"
                data['user_display_name'] = str(enteredUsername)
                token = str(uuid.uuid4())
                # loginTokens[enteredUsername] = token
                ttl = dt.timedelta(seconds=86400)  # 86400 seconds in a day (to set to expire at the end of the day)
                cacheTokens.setex(enteredUsername, ttl, value=token)
                data['token'] = token
            else:
                data['login'] = "not_authenticated"
                data['errorMessage'] = "Username and/or Password is Incorrect"
        else:
            data['login'] = "not_authenticated"
            data['errorMessage'] = "Username and/or Password is Incorrect"
        return data

    except Exception as e:
        return {"error": str(e)}
