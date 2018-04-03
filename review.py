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

#access website
driver.get('http://www.yelp.com')

#find and click login icon


print("Finding log in button")
icon=driver.find_element_by_id('header-log-in')
icon.click()

#print("Switching to pop up")
#find and switch to the popup fram

print("Filling email")

wait = WebDriverWait(driver, 10)

email=driver.find_elements_by_name("email")
for element in email:
    try:
        element.send_keys('shivahw040218@gmail.com')
    except:
        pass

password=driver.find_elements_by_name("password")
for element in password:
    try:
        element.send_keys('ilovecoding')
    except:
        pass


login=driver.find_elements_by_class_name('ybtn ybtn--primary ybtn--big submit ybtn-full')
for button in login:
    try:
        button.click()
    except:
        pass


"""



print("Filling password")
#find and fill the password box
pswd=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
pswd.send_keys('ilovecoding')

print("Click log in")
#find and click the login button
button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ybtn ybtn--primary ybtn--big submit ybtn-full')))
button.click()

def login():
    pass


#find and click the Restaurants button
myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'global-nav-restaurants')))

el=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'global-nav-restaurants')))
el.click()

#find and fill the search box
#searchBox=driver.find_element_by_class_name('typeahead_input')
searchBox=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'typeahead_input')))
searchBox.send_keys('Hoboken')

#find and click the search button
button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'SUBMIT_RESTAURANTS')))
button.click()

#wait until the page loads
myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'property_title')))

#find all the restaurants in the first page and print their names
els=driver.find_elements_by_class_name('property_title')
for el in els:
    print (el.text)
"""


if __name__ == "__main":
    login()