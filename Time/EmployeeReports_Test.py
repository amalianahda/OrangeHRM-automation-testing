import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com"
username="Admin"
password="admin123"

class EmployeeReports(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(5)


    def test_time_EmployeeReports(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.ID, "menu_time_viewTimeModule").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_time_Reports").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_time_displayEmployeeReportCriteria").click()
        time.sleep(0.5)
        driver.find_element(By.NAME, "time[employee][empName]").send_keys("Nahda")
        time.sleep(0.5)
        driver.find_element(By.ID, "viewbutton").click()
        time.sleep(2)
        
        notification = driver.find_element(By.CSS_SELECTOR,".validation-error").text
        self.assertIn(notification, "Invalid")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()