from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    button_signindropdown_xpath = "//button[@id='acUserMenu-aco']//div[@class='abc-ripple-wrapper']"
    button_signin_xpath = "//button[@id='acUserMenu-signIn']//div[@class='abc-ripple-wrapper']"
    textbox_username_xpath = "(//input[@type='text'])[13]"
    textbox_password_xpath = "(//input[@type='password'])[13]"
    button_login1_xpath = "(//input[@value='Sign in'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def signindropdown(self):
        self.driver.find_element(By.XPATH, self.button_signindropdown_xpath).click()

    def signin(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()

    def setusername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def login1(self):
        self.driver.find_element(By.XPATH, self.button_login1_xpath).click()
