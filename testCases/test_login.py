import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
import time
from selenium.webdriver.support import expected_conditions as EC


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(25)

        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(25)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.clickLogin()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCyProtect()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Cyber Protect Console":
            assert True
        else:
            assert False
