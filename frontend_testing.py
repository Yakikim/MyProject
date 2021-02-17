"""
for executing the frontend testing
:return:
"""
import selenium
from selenium import webdriver




def selenium_test(user_id):
    """
:param user_id:
:return: user_name
    """
    user_name = ''
    try:
        driver = selenium.webdriver.Firefox(
                executable_path="C:/Users/yakik/OneDrive/Documents/PycharmProjects/pythonProject1/geckodriver.exe")
        driver.get(f"http://127.0.0.1:5001/users/get_user_data/{user_id}")
        elmt = driver.find_element_by_id("user")
        user_name = elmt.text
        driver.close()
    except selenium.common.exceptions.NoSuchElementException as e:
        raise Exception("test failed")
    return (user_name)

if __name__ == '__main__':
    print(selenium_test(1))