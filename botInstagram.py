from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time



class InstaBot:
    def __init__(self, username, password):
        self.browser = Chrome()
        self.username = username
        self.password = password


    def login(self):

        user_element = 'username' #name
        pw_element = 'password' #name
        bt_entrar = 'sqdOP.L3NKy.y3zKF' #button - class

        browser = self.browser
        browser.get('https://www.instagram.com/')
        time.sleep(5)
        

        campo_user = browser.find_element_by_name(user_element)
        campo_user.send_keys(self.username)


        campo_passwd = browser.find_element_by_name(pw_element)
        campo_passwd.send_keys(self.password)

        bt_entrar = browser.find_element_by_class_name(bt_entrar)


        time.sleep(3)

        bt_entrar.click()
        

    def search(self, hashtag):
        browser = self.browser
        browser.get('https://www.instagram.com/explore/tags/' +hashtag+'/')
        time.sleep(5)






bot = InstaBot('', '') #instancia a classe - use como argumentos usuário e senha da conta do instagram

bot.login()