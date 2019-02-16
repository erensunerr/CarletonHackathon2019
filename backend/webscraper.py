from selenium import webdriver
from selenium.webdriver.common.keys import Keys

GOOGLE_URL = 'www.google.com'
GOOGLE_SEARCH_URL = 'www.google.com/search?q='

class ScrapeEngine:

    driver = None

    def __init__(self):
        print('constructing')
        options = webdriver.ChromeOptions()
        options.headless = True

        # chrome_driver_path = '/Users/oscarsplitfire/cuHacking2019/webdriver/chromedriver'
        chrome_driver_path = '../webdriver/chromedriver'

        self.driver = webdriver.Chrome(chrome_driver_path, options=options)

    def close(self):
        self.driver.close()

    def __del__(self):
        self.close()

    def goto(self, url: str):
        self.driver.get(url)

    def google_search(self, query: str):
        self.driver.get(GOOGLE_SEARCH_URL + query)










