from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(self):
    s = Service("C:\\Users\\Ibrahem.taha\\PycharmProjects\\pythonProject2\\drivers\\chromedriver.exe")
    self.driver = webdriver.Chrome(service=s)
    self.driver.implicitly_wait(25)
    return self.driver