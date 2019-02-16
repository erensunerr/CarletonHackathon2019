from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#chrome_driver_path = '/Users/oscarsplitfire/cuHacking2019/webdriver/chromedriver'
chrome_driver_path = '../webdriver/chromedriver'

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://www.python.org")

print(driver.title)

driver.close()
