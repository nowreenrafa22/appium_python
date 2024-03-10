import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import csv

def read_csv_file(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            return {'Review': row[0], 'Review text': row[1], 'Rating': row[2]
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
def test_review():
    flag = False
    review_description = read_csv_file('review.csv')
    review = review_description.get('Review')
    review_text = review_description.get('Review text')
    rating = review_description.get('Rating')

    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='NopStation Cart')
    driver.implicitly_wait(5)
    el.click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nokia Lumia 1020")').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/ratingBar").click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnAddReview").click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etReviewTitle").send_keys(review)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etReviewText").send_keys(review_text)
    time.sleep(2)

    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("com.nopstation.nopcommerce.nopstationcart:id/ratingBar").className("android.widget.RatingBar")').send_keys(rating)
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnSubmit").click()
    flag = False
    flag = True
    with open('giveReview_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Test Results'])
        if flag:
            writer.writerow(['Success'])
        else:
            writer.writerow(['Failure'])
    driver.quit()