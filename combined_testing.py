"""
The final testing of the program
include backend + frontend testing
"""
import backend_testing, frontend_testing

if __name__ == '__main__':
    user_id = 11 # input("Set user_id:")
    user_name = 'Yanbkle' #input("set user_name:")
    #backend_testing.delete_all()
    backend_testing.post(user_id, user_name)
    if backend_testing.get(user_id) != user_name:
        raise Exception(f"test failed GET: {user_id}, {user_name}")
    if backend_testing.query(user_id) != user_name:
        raise Exception(f"test failed QUERY: {user_id}, {user_name}")
    if frontend_testing.selenium_test(user_id) != user_name:
        raise Exception(f"test failed SLENIUM_TEST: {user_id}, {user_name}")
