from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='class')
def setup():
    s = Service("C:\\Users\\Ibrahem.taha\\PycharmProjects\\pythonProject2\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(25)
    return driver
