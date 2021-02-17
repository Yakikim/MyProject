"""
Backend Testing is for testing the rest_app.py module
"""
import requests
import db_connector as connector


base_path = 'http://127.0.0.1:5000/users'

def query(user_id):
    """

    :param user_id:
    :return: user_name
    """
    connector.my_db_cursor.execute(f"select user_name from {connector.db_user}.users where user_id = {user_id} ;")
    if connector.my_db_cursor.rowcount == 0:
        raise Exception("test failed")
    for row in connector.my_db_cursor:
        return (row[0])


def get(user_id):
    """
    :param user_id:
    :return: user_name
    """
    resp = requests.get(f"{base_path}/{user_id}")
    if resp.status_code != 200:
        raise Exception("test failed")
    return(resp.json().get("user_name"))

def post(user_id, user_name):
    """
    insert the user_id and the user_name into the users table
    :param user_id:
    :param user_name:
    """
    resp = requests.post(f"{base_path}/{user_id}", json={"user_name": f"{user_name}"})
    if resp.status_code != 200:
        raise Exception("test failed")
    return (resp.text)

def put(user_id, user_name):
    """
    insert the user_id and the user_name into the users table
    :param user_id:
    :param user_name:
    """
    resp = requests.put(f"{base_path}/{user_id}", json={"user_name": f"{user_name}"})
    if resp.status_code != 200:
        raise Exception("test failed")
    return (resp.text)

def delete_all():
    """
    delete all records of users table
    :return: success
    """
    connector.my_db_cursor.execute(f"delete from {connector.db_user}.users ;")
    return "success"


if __name__ == '__main__':
#    put(3, "jimi")
#   print(query(3))
    print(get(2))
#    post(6, 'Johny')
#    print(query(6))
#    if 1 == 1:
#        raise Exception("no")