import pytest
import time
from pageobject.LoginPage import Login
from selenium import webdriver
from utilities.readproperties import ReadConfig


class Test_005_createnewitem:
    baseURL = ReadConfig.getapplicationURL()
    username = "manvinder614@gmail.com"
    password = "Mannu@614"

    def test_newitem(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)