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

class MyInfo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(5)


    def test_MyInfo_bloodType(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "btnEditCustom").click()
        time.sleep(0.5)
        Select(driver.find_element(By.NAME, "custom1")).select_by_value("A-")
        driver.find_element(By.ID, "btnEditCustom").click()
        time.sleep(2)
        
        latest_blood_type = Select(driver.find_element(By.NAME, "custom1")).first_selected_option.text
        self.assertIn(latest_blood_type, "A-")

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()