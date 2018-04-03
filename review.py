from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#make browser
ua=UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
driver = webdriver.Chrome('/home/sarath/Documents/Shiva/shiva_040218/chromedriver',desired_capabilities=dcap,service_args=service_args)

driver.get('http://www.yelp.com')

def login(username, password_value):

    print("Finding log in button")
    icon=driver.find_element_by_id('header-log-in')
    icon.click()

    print("Filling email")
    wait = WebDriverWait(driver, 10)
    email = driver.find_elements_by_name("email")

    for element in email:
        try:
            element.send_keys(username)
        except:
            pass

    password=driver.find_elements_by_name("password")

    for element in password:
        try:
            element.send_keys(password_value)
            element.send_keys(Keys.TAB)
            element.send_keys(Keys.RETURN)
        except:
            pass


def submitReview(rev_text, rev_rating, restaurantID):
    pass


def vote(userID):
    pass


def test(username,password,rev_text, rev_rating, restaurantID, userID):
    pass


if __name__ == "__main__":
    login('shivahw040218@gmail.com', 'ilovecoding')
    #submitReview()