from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import os



class zapzap:
    #onde será executado o script
    dir_path = os.getcwd()

    #caminho do driver do navegador
    f_driver = os.path.join(dir_path, "geckodriver.exe")

    #caminho da pasta profile(dados do navegador)
    profile = os.path.join(dir_path, "profile", "wpp")

    def __init__(self):
        #configurações do navegador
        self.options = webdriver.FirefoxOptions()

        #configuração da pasta profile
        self.options.add_argument(r"user-data-dir={}".format(self.profile))

        #iniciar
        self.driver = webdriver.Firefox(self.f_driver, options=self.options)

        #acessando o web.whatsapp
        self.driver.get("https://web.whatsapp.com/")
        
        self.driver.inplicitly_wait(15)

    def abre_conversa(self, contato):
        try:
            #procura a caixa de pesquisa
            self.caixa_de_pesquisa = self.driver.find_element(By.CLASS_NAME, value="jN-F5")

            #digita o nome ou numero de contato
            self.caixa_de_pesquisa.send_keys(contato)
            sleep(2)

            #seleciona o contato
            self.contato = self.driver.find_element(By.XPATH, value="//span[@title = '{}']".format(contato))
            self.contato.click()
        except Exception as e:
            raise e
        
        raise e
    
