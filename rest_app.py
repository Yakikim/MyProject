"""
this module is the main web-server of the project.
 its can be called through the HTTP methods below and availabole at: http://127.0.0.1:5000/users
"""
from flask import Flask, request
import json
import datetime
from db_connector import select, insert, update, delete



app = Flask(__name__)
@app.route("/users/<user_id>",methods=['POST', 'GET', 'PUT', 'DELETE'])
def users(user_id):
    """
1.  POST – will accept user_name parameter inside the JSON payload.
        A new user will be created in the database (Please refer to Database section) with the
        id passed in the URL and with user_name passed in the request payload.
        ID has to be unique!
    On success: return JSON : {“status”: “ok”, “user_added”: <USER_NAME>} + code: 200
    On error: return JSON : {“status”: “error”, “reason”: ”id already exists”} + code: 500
2.  GET – returns the user name stored in the database for a given user id.
        Following the example: 127.0.0.1:5000/users/1 will return john.
    On success: return JSON : {“status”: “ok”, “user_name”: <USER_NAME>} + code: 200
    On error: return JSON : {“status”: “error”, “reason”: ”no such id”} + code: 500
3.  PUT – will modify existing user name (in the database).
        Following the above example, when posting the below JSON payload to
        127.0.0.1:5000/users/1
        george will replace john under the id 1
        {“user_name”: “george”}
    On success: return JSON : {“status”: “ok”, “user_updated”: <USER_NAME>} + code: 200
    On error: return JSON : {“status”: “error”, “reason”: ”no such id”} + code: 500
4.  DELETE – will delete existing user (from database).
        Following the above (marked) example, when using delete on 127.0.0.1:5000/users/1
        The user under the id 1 will be deleted.
    On success: return JSON : {“status”: “ok”, “user_deleted”: <USER_ID>} + code: 200
    On error: return JSON : {“status”: “error”, “reason”: ”no such id”} + code: 500
"""
    if request.method == 'POST':
        my_data = request.json
        user_name = my_data.get("user_name")
        mycon = select("'Y'", "users", f"user_id = {user_id}")
        if mycon.rowcount > 0:
            return json.dumps({'status': 'error', 'reason': "ID already exists"}), 500
        else:
            insert("users","user_id,user_name,creation_date",f"{user_id}, '{user_name}', '{datetime.datetime.now()}'")
            return json.dumps({'status': 'ok', 'user_added': user_name}), 200
    elif request.method == 'GET':
        mycon = select("'Y'", "users", f"user_id = {user_id}")
        if mycon.rowcount > 0:
            for row in mycon:
                return json.dumps({'status': 'ok', 'user_name': row[0]}), 200
        else:
            return json.dumps({'status': 'error', 'reason': "No such ID"}), 500
    elif request.method == 'PUT':
        my_data = request.json
        user_name = my_data.get("user_name")
        mycon = select("'Y'", "users", f"user_id = {user_id}")
        if mycon.rowcount > 0:
            update("users", f"user_name = '{user_name}'",  f"user_id = {user_id}")
            return json.dumps({'status': 'ok', 'user updated': user_name}), 200
        else:
            return json.dumps({'status': 'error', 'reason': "No such ID"}), 500
    elif request.method == 'DELETE':
        mycon = select("'Y'", "users", f"user_id = {user_id}")
        if mycon.rowcount > 0:
            delete("users", f"user_id = {user_id}")
            return json.dumps({'status': 'ok', 'user deleted': user_id}), 200
        else:
            return json.dumps({'status': 'error', 'reason': "No such ID"}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=5000)


