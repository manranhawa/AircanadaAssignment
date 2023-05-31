from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select


class Signup:
    button_signindropdown_xpath = "//button[@id='acUserMenu-aco']//div[@class='abc-ripple-wrapper']"
    button_joinin_xpath = "//button[@aria-labelledby='acUserMenu-joinNowContent']//abc-ripple//div"
    textbox_username_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    checkbox_accept_xpath = "//span[@class='mat-checkbox-inner-container']"
    button_continue_xpath = "//button[@type='submit']"
    textbox_Firstname_name = "firstName"
    textbox_Lastname_name = "lastName"
    dropdown_gender_xpath = "(//div)[219]"
    dropdown_language_xpath = "(//div)[236]"
    dropdown_day_xpath = "(//div)[246]"
    dropdown_month_xpath = "(//span)[45]"
    dropdown_year_xpath = "(//div)[268]"
    button_continue2_xpath = "//div[normalize-space()='Continue']"
    textbox_address_xpath = "//input[@type='text'])[2]"
    textbox_city_xpath = "//input[@formcontrolname='city'])[1]"
    dropdown_country_xpath = "(//div)[235]"
    dropdown_province_xpath = "(//div)[251]"
    textbox_phoneNumber_xpath = "(//input[contains(@aria-label,'Phone number')])"
    checkbox_accept2_xpath = "//span[contains(@class,'mat-checkbox-inner-container')]"
    checkbox_robot_xpath = "//div[@class='recaptcha-checkbox-border']"
    button_create_xpath = "//div[contains(text(),'Create my account')]"

    def __init__(self, driver):
        self.driver = driver

    def signindropdown(self):
        self.driver.find_element("xpath", self.button_signindropdown_xpath).click()

    def joinin(self):
        self.driver.find_element("xpath", self.button_joinin_xpath).click()

    def username(self, username):
        self.driver.find_element("xpath", self.textbox_username_xpath).clear()
        self.driver.find_element("xpath", self.textbox_username_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element("xpath", self.textbox_password_xpath).clear()
        self.driver.find_element("xpath", self.textbox_password_xpath).send_keys(password)

    def accchkbox(self):
        self.driver.find_element("xpath", self.checkbox_accept_xpath).click()

    def contin(self):
        self.driver.find_element("xpath", self.button_continue_xpath).click()

    def firstname(self, Firstname):
        self.driver.find_element("name", self.textbox_Firstname_name).clear()
        self.driver.find_element("name", self.textbox_Firstname_name).send_keys(Firstname)

    def lastname(self, lastname):
        self.driver.find_element("name", self.textbox_Lastname_name).clear()
        self.driver.find_element("name", self.textbox_Lastname_name).send_keys(lastname)

    def gender(self):
        self.driver.find_element("xpath", self.dropdown_gender_xpath).click()
        self.driver.find_element("xpath", '//body//div//mat-option[2]]').click()

    def day(self):
        self.driver.find_element("xpath", self.dropdown_day_xpath).click()


    def month(self):
        self.driver.find_element("xpath", self.dropdown_month_xpath).click()

    def year(self):
        self.driver.find_element("xpath", self.dropdown_year_xpath).click()

    def contin2(self):
        self.driver.find_element("xpath", self.button_continue2_xpath).click()

    def address(self, address):
        self.driver.find_element("name", self.textbox_username_xpath).clear()
        self.driver.find_element("name", self.textbox_username_xpath).send_keys(address)
        self.driver.find_element("name", self.textbox_username_xpath).send_keys(keys.ENTER)

    def cellnumber(self, phonenumber):
        self.driver.find_element("xpath", self.textbox_phoneNumber_xpath).clear()
        self.driver.find_element("xpath", self.textbox_phoneNumber_xpath).send_keys(phonenumber)

    def accchkbox2(self):
        self.driver.find_element("xpath", self.checkbox_accept2_xpath).click()

    def robot(self):
        self.driver.find_element_by_id("xpath", self.checkbox_robot_xpath).click()

    def create(self):
        self.driver.find_element("xpath", self.button_create_xpath).click()
