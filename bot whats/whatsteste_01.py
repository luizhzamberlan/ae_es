from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

class zapzap:
    def __init__(self):
        
        #Options
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("user-data-dir={}".format("./User_Data"))
        self.options.add_argument("--allow-profiles-outside-user-dir")

        #init
        self.driver = webdriver.Firefox(options=self.options)

        #acesso
        self.driver.get("https://web.whatsapp.com/")

        #wait scan qrcode
        input("Press ENTER to continue ----------------------------")


if __name__ == '__main__':
    bot = zapzap()
