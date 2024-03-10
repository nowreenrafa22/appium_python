import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
import csv

def test_device_setup():
    global driver
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
    }

    url = 'http://localhost:4723'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
def test_add_to_cart():
    flag = False
    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='NopStation Cart')
    driver.implicitly_wait(5)
    el.click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Category').click()

    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@resource-id="com.nopstation.nopcommerce.nopstationcart:id/categoryContainer"]/android.view.ViewGroup[7]').click()
    time.sleep(2)

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Mattress Bedroom"))')

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mattress Bedroom")').click()
    time.sleep(2)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("+"))')

    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnPlus").click()
    time.sleep(2)

    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnAddToCart").click()
    flag = True
    with open('add_to_cart_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Test Results'])
        if flag:
            writer.writerow(['Success'])
        else:
            writer.writerow(['Failure'])
    driver.quit()