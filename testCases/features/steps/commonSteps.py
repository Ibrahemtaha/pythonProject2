from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from behave import *

from utilities.readProperties import ReadConfig
baseURL = ReadConfig.getApplicationURL()


class commonSteps:
    @Given('Lunch Chrome Browser')
    def intialize_chrome(self):
        s = Service("C:\\Users\\Ibrahem.taha\\PycharmProjects\\pythonProject2\\drivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(25)
        self.driver.get(baseURL)
        return self.driver
