from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from time import sleep
import os



class zapzap:
    #onde será executado o script
    dir_path = os.getcwd()

    #caminho do driver do navegador

    #caminho da pasta profile(dados do navegador)
    profile = os.path.join(dir_path, "profile", "wpp")

    def __init__(self):
        self.service = Service(executable_path="./geckodriver.exe")

        #configurações do navegador
        self.options = webdriver.FirefoxOptions()

        #configuração da pasta profile
        self.options.add_argument(r"user-data-dir={}".format(self.profile))

        #iniciar
        self.driver = webdriver.Firefox(options=self.options)

        #acessando o web.whatsapp
        self.driver.get("https://web.whatsapp.com/")
        
        WebDriverWait(self.driver, 15)

    def abre_conversa(self, contato):
        try:
            #procura a caixa de pesquisa
            self.caixa_de_pesquisa = self.driver.find_element(By.CLASS_NAME, "jN-F5")

            #digita o nome ou numero de contato
            self.caixa_de_pesquisa.send_keys(contato)
            sleep(2)

            #seleciona o contato
            self.contato = self.driver.find_element(By.XPATH, "//span[@title = '{}']".format(contato))
            self.contato.click()
        except Exception as e:
            raise e
        
        raise e
    def envia_msg(self, msg):
        try:
            sleep(2)

            #seleciona a caixa de msg
            self.caixa_de_mensagem = self.driver.find_element(By.CLASS_NAME, "_2S1VP")

            #digita a msg
            self.caixa_de_mensagem.send_keys(msg)
            sleep(1)

            #botao enviar
            self.botao_enviar = self.driver.find_element(By.CLASS_NAME, "_35EW6")

            #send msg
            self.botao_enviar.click()
            sleep(2)
        
        except Exception as e:
            print("erro no envio da msg", e)

    def ultima_msg(self):
        try:
            post = self.driver.find_elements(By.CLASS_NAME, "_3_7SH")
            ultimo = len(post) -1

            #converter em texto
            texto = post[ultimo].find_element(By.CSS_SELECTOR, "span.selectable-text").text
            return texto

        except Exception as e:
            print('Erro ao ler a msg')

#Init bot

if __name__ == '__main__':
    bot = zapzap()
    bot.abre_conversa("bot teste") #grupo
    bot.envia_msg('Bot Initial test, everyone.. be proud')
    msg = ""
    while msg != "/quit":
        sleep(1)
        msg = bot.ultima_msg() #a cada loop le a msg

        if msg == "/help":
            bot.envia_msg("""
                          lets try it
                          /help
                          /code
                          /fun
                          /quit
                          """)
        elif msg == "/code":
            bot.envia_msg('logo a gente faz isso funfar')
        elif msg == '/fun':
            bot.envia_msg('paitrão é tipo um pai pra nozes')
        elif msg == '/quit':
            bot.envia_msg('chega por hj né? q a máquina n é de ferro... ou é?')
            exit
