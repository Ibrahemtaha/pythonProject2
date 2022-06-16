from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='session')
def setup():
    s = Service("C:\\Users\\Ibrahem.taha\\PycharmProjects\\pythonProject2\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    return driver

    # driver = webdriver.Chrome("C:\\Users\\Ibrahem.taha\\PycharmProjects\\pythonProject2\\drivers\\chromedriver.exe")
    # return driver
