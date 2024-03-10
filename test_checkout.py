import time
import csv
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
def read_csv_file(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            return {'First name': row[0], 'Last name': row[1], 'Email': row[2],
                    'Company': row[3], 'City': row[4], 'Street address': row[5],
                    'Street address 2': row[6], 'Zip / postal code': row[7],
                    'Phone number': row[8], 'Fax': row[9]
                    }

def test_device_setup():
    global driver
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
    }

    url = 'http://localhost:4723'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))


def test_checkout():
    flag = False
    information = read_csv_file('deliveryInfo.csv')
    first_name = information.get('First name')
    last_name = information.get('Last name')
    email = information.get('Email')
    company = information.get('Company')
    city = information.get('City')
    street_address = information.get('Street address')
    street_address_2 = information.get('Street address 2')
    postal_code = information.get('Zip / postal code')
    phone = information.get('Phone number')
    fax = information.get('Fax')

    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='NopStation Cart')
    driver.implicitly_wait(5)
    el.click()

    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/menu_cart").click()
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnCheckOut").click()
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout").click()
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etFirstName").send_keys(first_name)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etLastName").send_keys(last_name)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etEmail").send_keys(email)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/countrySpinner").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Bangladesh"))')
    driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="Bangladesh"])').click()
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/stateSpinner").click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Dhaka"))')
    driver.find_element(by=AppiumBy.XPATH,
                        value="//android.widget.TextView[@resource-id='android:id/text1' and @text='ঢাকা']").click()
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etCompanyName").send_keys(company)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')

    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etCity").send_keys(city)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress").send_keys(street_address)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress2").send_keys(street_address_2)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etZipCode").send_keys(postal_code)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etPhone").send_keys(phone)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etFax").send_keys(fax)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnContinue").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.RelativeLayout[@index='4']").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='CONTINUE']").click()
    time.sleep(1)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.RelativeLayout[@index='14']").click()

    driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.Button[@text='CONTINUE'])").click()

    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Next']").click()

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='CONFIRM']").click()
    time.sleep(3)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='CONTINUE']").click()
    flag = True
    with open('checkout_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Test Results'])
        if flag:
            writer.writerow(['Success'])
        else:
            writer.writerow(['Failure'])

    driver.quit()