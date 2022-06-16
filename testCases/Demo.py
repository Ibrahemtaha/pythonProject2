import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.ActiveAlertsSummary import ActiveAlertsSummary
import time
from selenium.webdriver.support import expected_conditions as EC

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    @pytest.fixture()
    def test_setup(self, setup):
        global driver
        driver = webdriver.Chrome("C:\\Users\\Ibrahem.taha\\PycharmProjects\\pythonProject2\\drivers\\chromedriver.exe")
        # self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.clickLogin()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickCyProtect()
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Cyber Protect Console":
            assert True
        else:
            assert False

        yield
        self.driver.close()
        self.driver.quit()
        print("Test Completed")



    def test_login(self, setup):
        print('any')
        # self.driver = setup
        # self.driver.implicitly_wait(15)
        # self.wait = WebDriverWait(self.driver, 25)
        # self.driver.get(self.baseURL)
        #
        # self.lp = LoginPage(self.driver)
        # self.lp.setUsername(self.username)
        # self.lp.clickLogin()
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        # self.lp.clickCyProtect()
        # act_title = self.driver.title
        # # self.driver.close()
        # if act_title == "Cyber Protect Console":
        #     assert True
        # else:
        #     assert False

    def test_checkWidgetExsist(self, setup):
        self.widget = ActiveAlertsSummary(self.driver, self.wait)
        self.widget.deleteWidget()

        # self.widget.editWidget()
        # self.widget.addWidget()
        # self.widget.searchInput()

        act_title = self.driver.title
        if act_title == "Cyber Protect Console":
            assert True
        else:
            assert False


    def test_teardown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")



