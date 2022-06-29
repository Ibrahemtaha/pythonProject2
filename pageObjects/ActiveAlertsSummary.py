import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait

class ActiveAlertsSummary:
    button_deleteWidget_xpath = "//div[contains(@title, 'Active alerts summary')]//following-sibling::div//button[@title = 'Delete']"
    button_editWidget_xpath = "//div[@title='Active alerts summary']//following-sibling::div//button[@title='Edit']"
    button_addWidget_xpath = "//button[@title=' Add widget '][@class='am-button am-button_variant_ghost qa-button']"
    input_search_xpath = "//input[@class='am-search-field__input']"
    div_activeAlertsWidget_xpath = "//div[@class='am-text am-text_body-accent'][@title='Active alerts summary']"
    widget_ActiveSummary_xpath = "//div[@title='Active alerts summary']"
    widget_Activities_xpath = "//div[@title='Activities']"
    widget_patchinstallationHistory_xpath = "//div[@title='Patch installation status']"
    iframe_xpath = "//iframe[@title='dashboard module']"
    widget_ActiveSummaryTitle_xpath = "//div[contains(@title, 'Active alerts summary')]"
    widget_ActivitiesTitle_xpath = "//div[contains(@title,'Activities')]"
    EditInputTitle_ActiveSummary_Xpath = "//div[@class='am-input am-input_size_ qa-input']/input[@type='text']"
    EditButtonDome_ActivSummary_Xpath = "//button[@type='submit'][@title=' Done ']"
    TitleSpan_AcitveSummary_Xpath = "//div[contains(@class, 'qa-active-alerts-summary-widget')]//div[@class='am-widget-panel__title qa-title sortable-handle']/span"
    AlertSeverityDropdown_ActiveSummary_Xpath = "//div[@class='am-dropdown__target qa-dropdown-target']//span[contains(text(),' Alert severity ')]"
    AlerttypeDropdown_ActiveSummary_Xpath = "//div[@class='am-dropdown__target qa-dropdown-target']//span[contains(text(),' Alert type')]"
    Warning_ActiveSummary_Xpath = "//span[@class='am-select__item_content am-text_ellipsis']//span[@title='Warning']"
    isDetected_ActiveSummary_Xpath = "//span[@class='am-select__item_content am-text_ellipsis']//span[@title='A malicious process is detected']"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait   = wait

    def deleteWidget(self, widget_name):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.iframe_xpath))  #SWITCH to iframe
        try:
            if (self.wait.until(EC.visibility_of_element_located((By.XPATH, self.widget_ActiveSummary_xpath)))):
                print("Active summary exist, Deleting the widget...")
                self.driver.find_element(By.XPATH, self.widget_ActiveSummaryTitle_xpath).click()
                self.driver.find_element(By.XPATH, self.button_deleteWidget_xpath).click()
                print("Widget has Deleted")
        except Exception as E:
            print("Active summary does not exist")
            self.addWidget(widget_name)
            self.deleteWidget(widget_name)

    def addWidget(self, widget_name):
        print("Adding new Widget")
        self.driver.find_element(By.XPATH, self.button_addWidget_xpath).click()
        self.driver.find_element(By.XPATH, self.input_search_xpath).click()
        self.driver.find_element(By.XPATH, self.input_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(widget_name)
        self.driver.find_element(By.XPATH, self.div_activeAlertsWidget_xpath).click()
        print("Widget Added")

    def moveWidget(self):
        print("Widget Will move")
        elem1 = self.driver.find_element(By.XPATH, self.widget_ActiveSummary_xpath)
        #elem2 = self.driver.find_element(By.XPATH, self.widget_patchinstallationHistory_xpath)
        location = elem1.location
        print(elem1.location)
        #print(elem2.location)
        time.sleep(4)
        elem1.click()
        ActionChains(self.driver).drag_and_drop_by_offset(elem1, location['x']+50, location['y']+0).perform()
        print("New Location = ")
        print(elem1.location)
        # ActionChains(self.driver).click_and_hold(elem1).move_to_element(elem2).release().perform()
        #ActionChains(self.driver).drag_and_drop(elem1, elem2).perform()
        print("Widget moved")
        print(elem1.location)
        #print(elem2.location)

    def editWidgetName(self, widget_nameNew):
        print("Widget to be edited")
        self.driver.find_element(By.XPATH, self.widget_ActiveSummaryTitle_xpath).click()
        self.driver.find_element(By.XPATH, self.button_editWidget_xpath).click()
        self.driver.find_element(By.XPATH, self.EditInputTitle_ActiveSummary_Xpath).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.EditInputTitle_ActiveSummary_Xpath))).clear()
        #self.driver.find_element(By.XPATH, self.EditInputTitle_ActiveSummary_Xpath).clear()
        self.driver.find_element(By.XPATH, self.EditInputTitle_ActiveSummary_Xpath).send_keys(widget_nameNew)
        self.driver.find_element(By.XPATH, self.EditButtonDome_ActivSummary_Xpath).click()
        print("Widget has been edited")
        # and Verify name entered if it's same
        newWidgetName = self.driver.find_element(By.XPATH, self.TitleSpan_AcitveSummary_Xpath).text
        if newWidgetName == widget_nameNew:
            assert True
        else:
            assert False

    def FilteringDisplayedData(self):
        self.driver.find_element(By.XPATH, self.widget_ActiveSummaryTitle_xpath).click()
        self.driver.find_element(By.XPATH, self.button_editWidget_xpath).click()
        ## to chose by value\ Visible Text \ by index
        # \ BY TITLE => change Xpath
        # \ Select \ Click


    def RedirectionFromWidget(self):
        print("123")
        try:  ## IF OR =>  more than one option, to click on it
            if (self.driver.find_element(By.XPATH, self.widget_ActiveSummaryTitle_xpath)):
                print("Active summary exist, Deleting the widget...")
                self.driver.find_element(By.XPATH, self.widget_ActiveSummaryTitle_xpath).click()
                self.driver.find_element(By.XPATH, self.button_deleteWidget_xpath).click()
                print("Widget has Deleted")
        except Exception as E:
            print("123")
            ### Add logger
            # + Is displayed()
    ### 3) add is_displayed(), is_checked(),
    ### Assert URL driver.current_url+ Page Title  .current_url
    ## https://github.com/mathare/selenium-python-pytest-bdd/blob/32411eb32969a0914a633a5fecf0d7b0f98052b7/pages/form_authentication.py#L38


    def searchInput(self, widgetName):
        self.driver.find_element(By.XPATH, self.input_searchButton_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_searchButton_xpath).send_keys(widgetName)


    # 1 def filterWidget(self):
    # 2 def RedirectWidget(self):
    # Verify link and title or similar things
    # 3 Close() quite() print("test comleted")
    # def setPassword(self,password):
    #     self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)



#https://selenium-python.readthedocs.io/locating-elements.html
# Check if the widget on the page -> if yes, then click delete
# assert url
#relaod after page
# yeild open once


### 0) finish the last 2 steps
### 1) Important: Confirmation messages, both Text & CSS color background (Mathare)
### 2) add assert text & CSS after each step, Verify Message and color
# https://github.com/mathare/selenium-python-pytest-bdd/blob/32411eb32969a0914a633a5fecf0d7b0f98052b7/step_defs/test_form_authentication_page_steps.py
### 2) Assert = in one line as in (Mathare)
### 3) add is_displayed(), is_checked(),is_selected() etc. (Mathare)
### 4) Add Logger instead of ptint - Part2 25 min + How to add multiple setLevel other than INFO
# https://www.youtube.com/watch?v=y2Kz3QaZcVo&list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf&index=2

#1) first issue  => we have to SWRICH method inside iframe

# git add .;git commit -m "newer"; git push