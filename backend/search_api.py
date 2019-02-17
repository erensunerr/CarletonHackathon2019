from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os


class searcher():
    """
    Google reverse image search bot
    Dependincies:
        - Selenium
        - Chrome Webdriver
    """

    def __init__(self):
        if 'linux' in sys.platform:
             os.chdir('../webdriver/linux')
        elif 'win' in sys.platform:
             os.chdir('../webdriver/win')
        elif 'darwin' in sys.platform:
             os.chdir('../webdriver/mac')

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)

    def __del__():
        self.driver.close()
searcher()
