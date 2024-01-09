import os
import time
from datetime import datetime

import pyautogui
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    __username_input = (By.ID, 'user-name')
    __password_input = (By.ID, 'password')
    __login_button = (By.ID, 'login-button')
    __error_message_container = (By.XPATH, '//div[@class = "error-message-container error"]')
    # __body = (By.TAG_NAME, 'body')

    # define locators
    def __init__(self, driver):
        self.driver = driver
    def login(self, username, password, ssIndex):
        self.driver.find_element(*self.__username_input).send_keys(username)
        self.driver.find_element(*self.__password_input).send_keys(password)
        self.driver.find_element(*self.__login_button).click()
        try:
            error = self.driver.find_element(*self.__error_message_container)
            if(error is not None):
                self.save_screenshot(f'loginPage{ssIndex}.png')
                print(error.text)
            return error
        except NoSuchElementException:
            return None
        except TimeoutException:
            print("Timeout occurred while searching for the element")
            return None

    def save_screenshot(self, name):
        time.sleep(2)
        now = datetime.now()
        # file_name = now.strftime("%d%m%Y%H%M%S") + "_" + name
        file_name = name
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f"{file_name}")
