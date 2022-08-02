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


    def test_Directory_invalidName(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.ID, "menu_directory_viewDirectory").click()
        time.sleep(0.5)
        driver.find_element(By.NAME, "searchDirectory[emp_name][empName]").send_keys("Nahda")
        time.sleep(0.5)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(2)
        
        search_result = driver.find_element(By.CSS_SELECTOR,".inner").text
        self.assertTrue(search_result)

    def test_Directory_validName(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.ID, "menu_directory_viewDirectory").click()
        time.sleep(0.5)
        driver.find_element(By.NAME, "searchDirectory[emp_name][empName]").send_keys("Odis Adalwin")
        time.sleep(0.5)
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(2)
        
        search_result = driver.find_element(By.CSS_SELECTOR,".odd")
        self.assertTrue(search_result)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()