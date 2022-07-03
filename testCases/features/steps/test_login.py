import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from behave import *
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
## First scenario
    @Given('Lunch Chrome Browser')
    def test_Display_Login_Page(self):
        setup(self)
        self.driver.get(baseURL)


    @Then('title should be "{expected_title}"')
    def test_Assert_Page_Title(self, expected_title):
        act_title = self.driver.title
        assert act_title == expected_title

## 2nd scenario
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

    # @Then("User should be navigated to Dashboard")


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

###
#1) @And doesnt work
#1) Params doesn't accept, like baseURL
#2) Assset title And sysntax in feature + test
#3) How to use the title method in methods
#4) OPTIMIZE - isSelected(),
#%) user title method from Page object to Assert in tests