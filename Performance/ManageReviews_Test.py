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

class ManageReviews(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self, driver):
        driver.find_element(By.NAME, "txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(5)


    def test_time_ManageReviews_invalidName(self):
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        self.login(driver)

        driver.find_element(By.ID, "menu__Performance").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_performance_ManageReviews").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_performance_searchPerformancReview").click()
        time.sleep(0.5)

        driver.find_element(By.NAME, "performanceReview360SearchForm[employeeName]").send_keys("Nahda")
        time.sleep(0.5)
        Select(driver.find_element(By.NAME, "performanceReview360SearchForm[jobTitleCode]")).select_by_value("7")
        time.sleep(0.5)
        Select(driver.find_element(By.NAME, "performanceReview360SearchForm[status]")).select_by_value("3")
        time.sleep(0.5)
        driver.find_element(By.ID, "btnSearch").click()
        time.sleep(2)
        
        search_result = driver.find_element(By.CSS_SELECTOR,"td").text
        self.assertTrue(search_result)

    def test_time_ManageReviews_validName(self):
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        self.login(driver)

        driver.find_element(By.ID, "menu__Performance").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_performance_ManageReviews").click()
        time.sleep(0.5)
        driver.find_element(By.ID, "menu_performance_searchPerformancReview").click()
        time.sleep(0.5)

        driver.find_element(By.NAME, "performanceReview360SearchForm[employeeName]").send_keys("Cecil Bonaparte")
        time.sleep(0.5)
        Select(driver.find_element(By.NAME, "performanceReview360SearchForm[jobTitleCode]")).select_by_value("7")
        time.sleep(0.5)
        Select(driver.find_element(By.NAME, "performanceReview360SearchForm[status]")).select_by_value("3")
        time.sleep(0.5)
        driver.find_element(By.ID, "btnSearch").click()
        time.sleep(0.5)
        
        search_result = driver.find_element(By.CSS_SELECTOR,".odd")
        self.assertTrue(search_result)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()