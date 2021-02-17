"""
this module is  The API gateway URL of the project.
 its can be called through the web browser and available at: http://127.0.0.1:5001/users/get_user_data/<user_id>
"""
from flask import Flask, request
import json
import requests

def get_user_name_from_db(user_id):
    """

    :param user_id:
    :return: user_name
    """
    res = requests.get(f"http://127.0.0.1:5000/users/{user_id}")
    my_data = res.json()
    if my_data.get("status") == "ok":
        return(my_data.get("user_name"))
    else:
        return(None)

my_app = Flask(__name__)
@my_app.route("/users/get_user_data/<user_id>")
def get_user_name(user_id):
    """
    :param user_id:
    :return: user_name or html error message
    """
    user_name = get_user_name_from_db(user_id)
    if user_name == None:
        return f"<H1 id='error'> no such user: {user_id} </H1>"
    else:
        return f"<H1 id='user'> {user_name} </H1>"

if __name__ == '__main__':
    my_app.run(host="127.0.0.1", debug=True, port=5001)


