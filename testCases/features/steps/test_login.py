import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from behave import *
# from pytest_bdd import *
from selenium.webdriver.chrome.service import Service
import time
from testCases.conftest import setup
from selenium.webdriver.support import expected_conditions as EC

baseURL = ReadConfig.getApplicationURL()
username = ReadConfig.getUseremail()
password = ReadConfig.getPassword()
### Logger
logger = LogGen.loggen()
#### Importing setup
# driver = setupClass.setup()


class Test_001_Login:



    @Then('title should be "{expected_title}"')
    def test_Assert_Page_Title(self, expected_title):
        act_title = self.driver.title
        assert act_title == expected_title

    @When('User Enters first "{username}"')
    def test_setUsername(self, username):
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(username)

    @When("User Click on Login Button")
    def test_ClickLoginButton(self):
        self.lp.clickLogin()

    @When('User Enters "{password}"')
    def test_setPassword(self, password):
        self.lp.setPassword(password)

    @When("User click on CyberProtect Button")
    def test_CyberProtect_Button(self):
        self.lp.clickCyProtect()

    @Then("User should be navigated to Dashboard")
    def test_Navigate_To_Dashboard(self):
        pass

    @Then('title should be here "{expected_title2}"')
    def test_Navigate_To_Dashboard(self, expected_title2):
        act_title2 = self.driver.title
        assert act_title2 == expected_title2


###
#2) Assset title And sysntax in feature + test
#3) How to use the title method in methods
#4) OPTIMIZE -,is_displayed(), is_checked(),is_selected()
#%) user title method from Page object to Assert in tests
#6) File Sturcutre
#7) Change behae lib to pytest-bdd


##8) Run test with Bahve AND Run Widget.py file with pytest
# First fix Fixure issue first (Widget run amd Behave doens't run
# 2nd: check can run behave and pytest widget file
