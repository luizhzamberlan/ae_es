import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

path = os.getcwd()
profile = os.path.join(path, "profile", "wpp")
options = webdriver.FirefoxOptions()
options.add_argument(r"user-data-dir={}".format(profile))
driver = webdriver.Firefox("./geckodriver.exe", options=options)

driver.get("https://web.whatsapp.com")

input('press ENTER after scanning')

search = driver.find_element(by='xpath', value='//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
search.send_keys('bot teste')

chat = driver.find_element(by='xpath', value="//span[@title='{}']".format('bot teste'))
chat.click()

last_text = driver.find_elements(by='xpath', value="//span[@class='_11JPr selectable-text copyable-text']")
text_list = []
for text in last_text:
    text_list.append(text.text)

if text_list[-1] == '/help':
    mensagem = "Como posso te ajudar?"
    text = driver.find_element(by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    text.send_keys(mensagem)
    driver.find_element(by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()

