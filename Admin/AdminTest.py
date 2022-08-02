import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

#variable
url="https://opensource-demo.orangehrmlive.com"
username="Admin"
password="admin123"

class AdminTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(5)

    def test_Admin_Localization(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_admin_Configuration").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_admin_localization").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(1)
        Select(driver.find_element(By.NAME, "localization[default_date_format]")).select_by_value("d-m-Y")
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)
        
        latest_date_format = Select(driver.find_element(By.NAME, "localization[default_date_format]")).first_selected_option.text
        self.assertIn(latest_date_format, "dd-mm-yyyy ( 01-08-2022 )")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()