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



        platform = ""


        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')

        os.chdir('../images_backend')
        self.image_dir = os.getcwd()
        print(self.image_dir)

        print(sys.platform)
        if 'linux' in sys.platform:
            platform = 'linux'
            self.driver = webdriver.Chrome('../webdriver/linux/chromedriver', options=options)

        elif 'win' in sys.platform:
            platform = 'win'
            print(os.chdir('../webdriver/win'))
            print(os.getcwd())
            self.driver = webdriver.Chrome('chromedriver.exe',options=options)

        elif 'darwin' is sys.platform:
            platform = 'mac'
            self.driver = webdriver.Chrome('../webdriver/mac/chromedriver', options=options)
        else:
            raise Exception("Platform not found")


    def __del__(self):
        self.driver.close()

    def __open_image_dialog(self):
        self.driver.get("https://www.google.com/imghp?hl=EN")
        cam_button = self.driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
        cam_button.click()
        upload_image = self.driver.find_elements_by_xpath("//div[@class=\"qbtbha sl\"]")[0]
        upload_image.click()
        self.upload_dialog = self.driver.find_elements_by_xpath("//input[@id=\"qbfile\" and @name=\"encoded_image\"]")[0]


    def text(self):
        return self.driver.text

    def upload_image(self,path):
        try:
            self.upload_dialog
        except:
            self.__open_image_dialog()
        self.upload_dialog.send_keys(self.image_dir+"/"+path)
        sleep(10)


s = searcher()
s.upload_image('bottle.bmp')
