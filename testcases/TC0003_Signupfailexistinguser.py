import pytest
import time
from pageobject.LoginPage import Login
from selenium import webdriver

from pageobject.Signup import Signup
from utilities.readproperties import ReadConfig


class Test_003_Signupexistinguser:
    baseURL = ReadConfig.getapplicationURL()

    def test_Signupexitinuser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(15)
        self.sp = Signup(self.driver)
        self.sp.signindropdown()
        self.sp.joinin()
        self.sp.username("officialmanvinder.qa@gmail.com")
        self.sp.setpassword("Mannu@614614")

        err_msg = "You have reached the maximum number of attempts to enroll; further attempts are now " \
                  "restricted.Please try again later."
        actual_msg =self.driver.find_element("xpath" , "//div[@class='alert-text']").text
        if err_msg==actual_msg:
            assert True
        else:
            assert False
