import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import csv

def test_device_setup():
    global driver
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android'
    }
    url = 'http://localhost:4723'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

def test_add_remove_wishlist():
    flag = False
    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='NopStation Cart')
    driver.implicitly_wait(5)
    el.click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nokia Lumia 1020")').click()
    time.sleep(4)
    driver.find_element(by=AppiumBy.XPATH, value= "//android.widget.ImageButton[@resource-id=\"com.nopstation.nopcommerce.nopstationcart:id/fabAddToWishlist\"]").click()

    time.sleep(5)
    driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.widget.ImageView[@resource-id=\"com.nopstation.nopcommerce.nopstationcart:id/navigation_bar_item_icon_view\"])[4]").click()
    time.sleep(5)
    driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.nopstation.nopcommerce.nopstationcart:id/tvOptionName\" and @text=\"Wishlist\"]").click()
    time.sleep(5)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/icRemoveItem").click()
    flag = True
    with open('add_remove_wishlist_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Test Results'])
        if flag:
            writer.writerow(['Success'])
        else:
            writer.writerow(['Failure'])
    driver.quit()