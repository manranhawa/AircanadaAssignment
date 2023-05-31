import pytest
import time
from pageobject.LoginPage import Login
from selenium import webdriver

from pageobject.Signup import Signup
from utilities.readproperties import ReadConfig


class Test_004_Signup:
    baseURL = ReadConfig.getapplicationURL()

    def test_Signup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(15)
        self.sp = Signup(self.driver)
        self.sp.signindropdown()
        self.sp.joinin()
        self.sp.username("officialmanvinder.qa@gmail.com")
        self.sp.setpassword("Mannu@614614")
        self.sp.accchkbox()
        self.sp.contin()
        self.sp.firstname('Manvinder')
        self.sp.lastname('Randhawa')
        self.sp.gender()
        self.sp.day()
        self.sp.month()
        self.sp.year()
        self.sp.contin2()
        self.sp.address('110 narrowvalley crescent')
        self.sp.cellnumber('4372148180')
        self.sp.accchkbox2()
        self.sp.create()






