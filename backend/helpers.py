# Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
# Helper code snippets, for each function

from logging import error
from tables import *
import datetime as dt
import uuid
from flask.globals import session
import redis

# from flask_table import Table, Col

session = Session()

loginTokens = {}
cacheTokens = redis.Redis()


def authenticateAPI(token):
    try:
        keys = cacheTokens.keys('*')
        for key in keys:
            if cacheTokens.get(key).decode() == str(token):
                return True
        return False
    except Exception as e:
        return {"error": str(e)}


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
                cacheTokens.setex(enteredUsername, ttl, value=token)  # token expires in a day
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


# Operations Page
# For choosing people with required skill sets for a project
# 1. Projects: Will show a list of ongoing projects - start date, end date and skillsets required
# 2. People: Show employee name, role, designation, skills
# 3. Pipeline: Show list of future projects - expected start date, skill sets required
def operationsProjects():
    # show list of of ongoing projects : start date, end date, skills required
    try:
        projects = session.query(Project).all()  # can be changed to query accordingly
        projectList = []
        for project in projects:
            temp = {'clientname': project.clientname, 'projectname':project.projectname,'startdate': project.startDate, 'enddate': project.endDate,'skillsrequired':project.skillsrequired, 'status': project.projectstatus}
            projectList.append(temp)
        return projectList
        # return render_template('display.html', columns=columns,table_data=table_d)
    except Exception as e:
        print(e)
        return {"error": str(e)}


def operationsPeople():
    # show employee name, role, designation, skill, project
    try:
        # if not authenticateAPI(token):
        #     return {"error": "Not Authenticated"}
        employees = session.query(Employee).all()  # can be changed to query accordingly
        employeeList = []
        for employee in employees:
            temp = {'name': employee.employee_name, 'role': employee.employee_role, 'designation': employee.designation,
                    'skill': employee.skill}
            employeeList.append(temp)
        return employeeList
        # return render_template('display.html', columns=columns,table_data=table_d)
    except Exception as e:
        print(e)
        return {"error": str(e)}
