import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from behave import *
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC


class Test_001_Login:
    # baseURL = ReadConfig.getApplicationURL()
    baseURL = "https://mc-vz7test20.do.acronis.fun/"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @Given('User is on Login page')
    def test_Display_Login_Page(self):
        s = Service("C:\\Users\\Ibrahem.taha\\PycharmProjects\\pythonProject2\\drivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(25)
        self.driver.get("https://mc-vz7test20.do.acronis.fun/")
        # self.driver.get(self.baseURL)
        time.sleep(5)

        # self.driver.get("https://mc-vz7test20.do.acronis.fun/")

    @And('title asserted "Login" "{act_title}"')
    def test_Assert_Page_Title(self, act_title):
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Login":
            assert True
        else:
            assert False
    def test_homePageTitle(self, setup):
        # self.driver = setup
        self.driver.implicitly_wait(25)
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Login":
            assert True
        else:
            assert False
        self.logger.info("********** Page title asserted *********")
        # self.logger.debug("**********  DEEEBBBBUUUGGGG *********")

    def test_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(25)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        assert self.lp.pageTitle() == "Login"

        self.lp.setUsername(self.username)
        self.lp.clickLogin()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCyProtect()
        act_title = self.driver.title
        #self.driver.close()
        #Make method for title => Here just assert
        if act_title == "Cyber Protect Console":
            assert True
        else:
            assert False

        self.driver.close()

        #  act_title = self.driver.title
        # if act_title == "Cyber Protect Console":
        #     assert True
        # else:
        #     assert False
