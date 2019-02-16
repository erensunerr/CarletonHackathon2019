from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = True

#chrome_driver_path = '/Users/oscarsplitfire/cuHacking2019/webdriver/chromedriver'
chrome_driver_path = '../webdriver/chromedriver'

driver = webdriver.Chrome(chrome_driver_path, options=options)

driver.get("http://www.python.org")


assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

print(driver.title)

assert "No results found." not in driver.page_source

driver.close()

