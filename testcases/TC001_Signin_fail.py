import pytest
import time
from pageobject.LoginPage import Login
from selenium import webdriver
from utilities.readproperties import ReadConfig


class Test_001_Loginfail:
    baseURL = ReadConfig.getapplicationURL()
    username = "manvinder614@gmail.com"
    password = "Mannu@614"

    def test_loginfail(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.lp = Login(self.driver)
        self.lp.signindropdown()
        time.sleep(2)
        self.lp.signin()
        time.sleep(15)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.button_login1_xpath()
        act_title = self.driver.title
        if act_title != "Aeroplan Everyday":
            assert True
        else:
            assert False
