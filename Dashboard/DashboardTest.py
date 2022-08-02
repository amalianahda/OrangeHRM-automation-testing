import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com"
username="Admin"
password="admin123"

class DashboardTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(5)
        driver.find_element(By.NAME,"Submit").click()

    def test_dashboard_timesheet(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.CSS_SELECTOR, ".quickLaunge").click()
        time.sleep(2)

        current_url = driver.current_url
        self.assertIn(current_url, "https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave")


    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()