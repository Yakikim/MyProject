"""
The final testing of the program
include backend + frontend testing
"""
import backend_testing, frontend_testing

if __name__ == '__main__':
    user_id = input("Set user_id:")
    user_name = input("set user_name:")
    #backend_testing.delete_all()
    backend_testing.post(user_id, user_name)
    if backend_testing.get(user_id) != user_name:
        raise Exception("test failed: ")
    if backend_testing.query(user_id) != user_name:
        raise Exception("test failed")
    if frontend_testing.selenium_test(user_id) != user_name:
        raise Exception("test failed")
