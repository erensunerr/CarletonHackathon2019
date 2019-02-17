from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os
from time import sleep

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
            options.add_argument('headless')
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


    def text(self):
        return self.driver.text

    def upload_image(self, path):
        try:
            self.upload_dialog
        except:
            self.__open_image_dialog()
        self.upload_dialog.send_keys(self.image_dir+"/"+path)


s = searcher()
s.upload_image('duck.jpg')

input()

print('opening shopping section')

s.open_shopping_section()

input()

print('closing up')

del s
