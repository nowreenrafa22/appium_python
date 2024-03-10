import pytest
import time
import csv
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

def read_csv_file(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            return {'user_email': row[0], 'password': row[1]}

def test_device_setup():
    global driver
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android'
    }
    url = 'http://localhost:4723'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

def test_login():
    flag = False
    login = read_csv_file('login.csv')
    user_email = login.get('user_email')
    password = login.get('password')
    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='NopStation Cart')
    driver.implicitly_wait(5)
    el.click()
    driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.nopstation.nopcommerce.nopstationcart:id/navigation_bar_item_icon_view\"])[4]").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.nopstation.nopcommerce.nopstationcart:id/tvOptionName\" and @text=\"Log in\"]").click()
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/loginEmailEditText").send_keys(user_email)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/loginPasswordEditText").send_keys(password)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/loginButton").click()
    driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.nopstation.nopcommerce.nopstationcart:id/navigation_bar_item_icon_view\"])[4]").click()
    flag = True
    with open('login_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Test Results'])
        if flag:
            writer.writerow(['Success'])
        else:
            writer.writerow(['Failure'])

    driver.quit()