import pytest
import time
from pageobject.LoginPage import Login
from selenium import webdriver
from utilities.readproperties import ReadConfig

class Test_002_Loginpass:
    baseURL = ReadConfig.getapplicationURL()
    username = "officialmanvinder.qa@gmail.com"
    password = "Mannu@614614"

    def test_loginpass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(15)
        self.lp = Login(self.driver)
        self.lp.signindropdown()
        self.lp.signin()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.button_login1_xpath()
        act_title = self.driver.title
        if act_title== "Aeroplan Everyday":
            assert True
        else:
            assert False

