from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    textbox_username_xpath = "//input[@aria-label='Login' and @name='username']"
    button_login_xpath = "//button[@type='submit']"
    textbox_password_xpath = "//input[@aria-label='Password' and @type='password']"
    button_logout_xpath = "//header/div[2]/button[1]/span[1]"
    button_cyprebProtection_xpath = "//body/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH, self. textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self. textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def clickCyProtect(self):
        self.driver.find_element(By.XPATH, self.button_cyprebProtection_xpath).click()


#https://selenium-python.readthedocs.io/locating-elements.html
# Check if the widget on the page -> if yes, then click delete


# yeild open once



