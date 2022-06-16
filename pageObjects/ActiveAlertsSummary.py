import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait

class ActiveAlertsSummary:
    button_deleteWidget_xpath = "//div[contains(@title, 'Active alerts summary')]//following-sibling::div//button[@title = 'Delete']"
    button_editWidget_xpath = "/html/body/am-app/am-dashboards/am-entry/div/am-dashboard-panel/div/am-scrollbar/div[2]/div/div/div/div/div/div/div[1]/am-widget-panel/div/am-widget-header/div/div[2]/div[1]/am-button/button"
    button_addWidget_xpath = "/html/body/am-app/am-dashboards/am-entry/div/am-dashboard-panel/div/div[2]/am-dashboard-toolbar/div/div[2]/div[1]/am-button/button"
    input_search_xpath = "//input[@class='am-search-field__input']"
    div_activeAlertsWidget_xpath = "//div[@class='am-text am-text_body-accent'][@title='Active alerts summary']"
    widget_ActiveSummary_xpath = "//div[@class='am-widget-panel am-widget-panel_height_s am-widget-panel_pie_chart am-flex-container qa-active-alerts-summary-widget am-widget-panel_mode_edit']"
    widget_Activities_xpath = "//div[@class='am-widget-panel am-widget-panel_height_s am-widget-panel_activity am-flex-container qa-activities-widget am-widget-panel_mode_edit']"
    widget_patchinstallationHistory_xpath = "//div[@class='am-widget-panel am-widget-panel_height_u am-widget-panel_table am-flex-container qa-patch-install-history-table-widget am-widget-panel_mode_edit']"
    iframe_xpath = "//iframe[@title='dashboard module']"
    widget_ActiveSummaryTitle_xpath = "//div[contains(@title, 'Active alerts summary')]"
    widget_ActivitiesTitle_xpath = "//div[contains(@title,'Activities')]"
    # button_cyprebProtection_xpath = "//body/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]"

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
        elem2 = self.driver.find_element(By.XPATH, self.widget_patchinstallationHistory_xpath)
        location = elem1.location
        print(elem1.location)
        print(elem2.location)
        time.sleep(4)
        elem1.click()
        # ActionChains(self.driver).drag_and_drop_by_offset(elem1, location['x']+100, location['y']+200).perform()
        # ActionChains(self.driver).click_and_hold(elem1).move_to_element(elem2).release().perform()
        ActionChains(self.driver).drag_and_drop(elem1, elem2).perform()
        print("Widget moved")
        print(elem1.location)
        print(elem2.location)

    def editWidgetName(self):
        print("Widget edited")
        self.driver.find_element(By.XPATH, self. button_editWidget_xpath).click()
        # and Verify name entered if it's same

    def searchInput(self, widgetName):
        self.driver.find_element(By.XPATH, self. input_searchButton_xpath).clear()
        self.driver.find_element(By.XPATH, self. input_searchButton_xpath).send_keys(widgetName)

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
#modify expath + rauhl shetty
# Use Logger instead of Print statemnts

#1) first Problem => we have to SWRICH method inside iframe