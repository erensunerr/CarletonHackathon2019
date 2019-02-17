from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os
from time import sleep

import base64

import urllib

class searcher():
    """
    Google reverse image search bot
    Dependincies:
        - Selenium
        - Chrome Webdriver
    """

    def __init__(self, headless=False):
        os.chdir('../images_backend')
        self.image_dir = os.getcwd()
        print(self.image_dir)

        platform = ""
        end = ""

        if 'linux' in sys.platform:
            platform = 'linux'
        elif 'win' in sys.platform and 'dar' not in sys.platform:
            end = '.exe'
            platform = 'win'
        elif 'dar' in sys.platform:
            platform = 'mac'


        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--window-size=1920,1080')
            options.add_argument('headless')
            options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome('../webdriver/' + platform + '/chromedriver' + end, options=options)


    def __del__(self):
        self.driver.close()

    def __open_image_dialog(self):
        self.driver.get("https://www.google.com/imghp?hl=EN")
        cam_button = self.driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
        cam_button.click()
        upload_image = self.driver.find_elements_by_xpath("//div[@class=\"qbtbha sl\"]")[0]
        upload_image.click()
        self.upload_dialog = self.driver.find_elements_by_xpath("//input[@id=\"qbfile\" and @name=\"encoded_image\"]")[0]


    def open_shopping_section(self):
        shop_button = self.driver.find_element_by_xpath(".//a[text()=\"Shopping\" and @class=\"q qs\"]")
        shop_button.click()


    def select_lo2hi(self):
        b1 = self.driver.find_element_by_xpath(".//span[@class=\"Yf5aUd\"]")
        b1.click()
        sleep(1)
        self.driver.find_element_by_xpath(".//g-menu-item[.//div[text()=\"PRICE – LOW TO HIGH\"]]").click()


    def text(self):
        return self.driver.text

    def upload_image(self, path):
        try:
            self.upload_dialog
        except:
            self.__open_image_dialog()
        self.upload_dialog.send_keys(self.image_dir + "/" + path)


s = searcher()

s.driver.get("http://127.0.0.1:5000/index")

canvas = s.driver.find_element_by_css_selector("#canvas")

# get the canvas as a PNG base64 string
canvas_base64 = s.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

# decode
canvas_png = base64.b64decode(canvas_base64)

with open("tempdel.png", 'wb') as fout:
    fout.write(canvas_png)
